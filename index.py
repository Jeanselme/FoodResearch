import os
import json
import bibtexparser
import pandas as pd

ref_folder = 'References'
index_file = pd.read_csv(os.path.join(ref_folder, 'index.csv'), index_col = 0, squeeze = True)

def new_files():
    """
        Verify if there is new files in the References folder
    """
    return len(index_file) < len([f for f in os.listdir(ref_folder) if '.bib' in f])

def update_index():
    for ref in [f for f in os.listdir(ref_folder) if '.bib' in f]:
        if not(ref in index_file.index):
            index_file.loc[ref] = pd.Timestamp.now()
    index_file.to_csv(os.path.join(ref_folder, 'index.csv'), header = True)

tags = {}
def generate_readme():
    """
        Parse files and generate markdown readme
    """
    with open("README.md", 'w') as readme:
        readme.write("# [Food Realted Research](https://jeanselme.github.io/FoodResearch/)\n\n")

        readme.write("## Articles\n\n")
        datasets = {}
        for i, ref in enumerate([f for f in os.listdir(ref_folder) if '.bib' in f]):
            # Bibtex
            bib = bibtexparser.load(open(os.path.join(ref_folder, ref), 'r'))
            assert len(bib.entries) > 0, "{} not in .bib format".format(ref)
            readme.writelines(from_bib_to_markdown(bib.entries[0], i + 1))

            # Notes
            notes = os.path.join(ref_folder, ref[:ref.index('.bib')] + '.notes')
            if os.path.isfile(notes):
                markdown = from_notes_to_markdown(json.load(open(notes, 'r')), i + 1)
                readme.writelines(markdown)

        # Tags
        readme.write("\n## Tags\n\n")
        for tag in tags:
            readme.writelines("#### {}\n\n".format(tag))
            readme.writelines(', '.join(["[\[{}\]](#{})".format(ind, ind) for ind in tags[tag]]) + '\n')

        update_index()
    return 0

def from_bib_to_markdown(bib, ind):
    """
        Transforms the json format into a nice markdown
    
        Arguments:
            bib {Dict} -- Dictionary return by bibtexparser

        Returns:
            Markdown text
    """
    markdown = "### <a name='{}'></a> \[{}\] [{}]({})\n".format(ind, ind, bib["title"], bib["url"])
    markdown += "by {}\nin {}\n\n".format(bib["author"], bib["year"])
    markdown += "#### Abstract\n"
    markdown += "> {}\n\n".format(bib["abstract"].replace('\n', '\n>'))
    return markdown

note_format = [	"Summary", "Conclusions", "Limitations", "Data", "Website"]
def from_notes_to_markdown(notes, ind):
    """
        Transforms the json format into a nice markdown
    
        Arguments:
            notes {Dict} -- Dictionary return by json

        Returns:
            markdown, datasets: mardown text and list of datasets linked to the article
    """
    global tags
    markdown = ""
    for cat in [nf for nf in note_format if nf in notes]:
        markdown += "#### {}\n".format(cat)
        if isinstance(notes[cat], list):
            for e in notes[cat]:
                markdown += "- {}\n".format(website_to_markdown(e))
        else:
            markdown += "{}\n".format(website_to_markdown(notes[cat]))
        markdown += "\n"

    if "Tags" in notes:
        markdown += "#### Tags\n"
        for tag in notes["Tags"]:
            markdown += "[\#{}](#{}) ".format(tag, tag)

            if tag in tags:
                tags[tag].append(ind)
            else:
                tags[tag] = [ind]

    markdown += "\n\n" 
    return markdown

def website_to_markdown(text):
    """
        Create a link of the text contains http://
    """
    if "http://" == text[:7]:
        text = "[{}]({})".format(text, text)
    return text