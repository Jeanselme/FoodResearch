# [Food Realted Research](https://jeanselme.github.io/FoodResearch/)

## Articles

### <a name='1'></a> \[1\] [You Tweet What You Eat](http://dx.doi.org/10.1145/2702123.2702153) 

by Abbar, Sofiane and Mejova, Yelena and Weber, Ingmar
 in 2015

#### Abstract
> Food is an integral part of our lives, cultures, and well-being, and is of major interest to public health. The collection of daily nutritional data involves keeping detailed diaries or periodic surveys and is limited in scope and reach. Alternatively, social media is infamous for allowing its users to update the world on the minutiae of their daily lives, including their eating habits. In this work we examine the potential of Twitter to provide insight into US-wide dietary choices by linking the tweeted dining experiences of 210K users to their interests, demographics, and social networks. We validate our approach by relating the caloric values of the foods mentioned in the tweets to the state-wide obesity rates, achieving a Pearson correlation of 0.77 across the 50 US states and the District of Columbia. We then build a model to predict county-wide obesity and diabetes statistics based on a combination of demographic variables and food names mentioned on Twitter. Our results show significant improvement over previous CHI research (Culotta'14). We further link this data to societal and economic factors, such as education and income, illustrating that, for example, areas with higher education levels tweet about food that is significantly less caloric. Finally, we address the somewhat controversial issue of the social nature of obesity (first raised by Christakis & Fowler in 2007) by inducing two social networks using mentions and reciprocal following relationships.

<details>
<summary>Notes</summary>

#### Summary
This article shows the correlation between content of tweets and obeity by county. From it it produces a model that produces a risk of obseity for each individual allowing the anlyasis of interest of high risk people. It finally explores the network of friends to see the spread of obesity thourh network.

#### Conclusions
- Strong correlation between food mentioned in tweets but also calories
- Demographic such as education and income have also a strong impact (even if only the mean by area is considered)
- People showing an interest in cooking have a lower risk in obesity
- High correlation with watching TV
- Friends are more likely to present a similar relation to food

#### Limitations
- Usual limitations of tweet: is it really reflective of habits (weekly in this dataset), selection bias, difference of tweets behavior given region
- Use #problemoffat is perhaps not nly used by obese people
- Use of model based on mean to predict personal risk: the use of image recognition to estimate the weight could enhance results)

#### Tags
[\#Obesity](#Obesity) [\#Social Network](#Social_Network) [\#Network](#Network) [\#USA](#USA) 
</details>

### <a name='2'></a> \[2\] [Large-scale and high-resolution analysis of food purchases and health outcomes](https://doi.org/10.1140/epjds/s13688-019-0191-y) 

by Aiello, Luca Maria and Schifanella, Rossano and Quercia, Daniele and Del Prete, Lucia
 in 2019

#### Abstract
> To complement traditional dietary surveys, which are costly and of limited scale, researchers have resorted to digital data to infer the impact of eating habits on people's health. However, online studies are limited in resolution: they are carried out at country or regional level and do not capture precisely the composition of the food consumed. We study the association between food consumption (derived from the loyalty cards of the main grocery retailer in London) and health outcomes (derived from publicly-available medical prescription records of all general practitioners in the city). The scale and granularity of our analysis is unprecedented: we analyze 1.6B food item purchases and 1.1B medical prescriptions for the entire city of London over the course of one year. By studying food consumption down to the level of nutrients, we show that nutrient diversity and amount of calories are the two strongest predictors of the prevalence of three diseases related to what is called the 'metabolic syndrome': hypertension, high cholesterol, and diabetes. This syndrome is a cluster of symptoms generally associated with obesity, is common across the rich world, and affects one in four adults in the UK. Our linear regression models achieve an R^2 of 0.6 when estimating the prevalence of diabetes in nearly 1000 census areas in London, and a classifier can identify (un)healthy areas with up to 91% accuracy. Interestingly, healthy areas are not necessarily well-off (income matters less than what one would expect) and have distinctive features: they tend to systematically eat less carbohydrates and sugar, diversify nutrients, and avoid large quantities. More generally, our study shows that analytics of digital records of grocery purchases can be used as a cheap and scalable tool for health surveillance and, upon these records, different stakeholders from governments to insurance companies to food companies could implement effective prevention strategies.

<details>
<summary>Notes</summary>

#### Summary
This article uses grocery store data and medical prescriptions to analyze the impact of food on metabolic syndrom in London.

#### Conclusions
- Socio economic conditons impacts less than nutritions
- Eating less and diverse nutrients is linked to better health conditions
- Calorie concentration is more important than calorie consumption

#### Limitations
- Selection bias: population are limited to a grocery and only people with loyalty card are concerned
- No causal explanation

#### Website
[http://goodcitylife.org/food/project.php](http://goodcitylife.org/food/project.php)

#### Tags
[\#Obesity](#Obesity) [\#Grocery](#Grocery) [\#ML](#ML) [\#England](#England) 
</details>

### <a name='3'></a> \[3\] [Nutritional content of supermarket ready meals and recipes by television chefs in the United Kingdom: cross sectional study](https://www.semanticscholar.org/paper/Nutritional-content-of-supermarket-ready-meals-and-Howard-Adams/7a329e67996f55433b606d250c9edb05b11b7582) 

by Simon James Howard and Jean Adams and Michel White
 in 2012

#### Abstract
> OBJECTIVES
>To compare the energy and macronutrient content of main meals created by television chefs with ready meals sold by supermarkets, and to compare both with nutritional guidelines published by the World Health Organization and UK Food Standards Agency.
>
>
>DESIGN
>Cross sectional study.
>
>
>SETTING
>Three supermarkets with the largest share of the grocery market in the United Kingdom, 2010.
>
>
>SAMPLES
>100 main meal recipes from five bestselling cookery books by UK television chefs and 100 own brand ready meals from the three leading UK supermarkets.
>
>
>MAIN OUTCOME MEASURES
>Number of meals for which the nutritional content complied with WHO recommendations, and the proportion of nutrients classified as red, amber, or green using the UK FSA's "traffic light" system for labelling food.
>
>
>RESULTS
>No recipe or ready meal fully complied with the WHO recommendations. The ready meals were more likely to comply with the recommended proportions of energy derived from carbohydrate (18% v 6%, P=0.01) and sugars (83% v 81%, P=0.05) and fibre density (56% v 14% P<0.01). The recipes were more likely to comply with the recommended sodium density (36% v 4%, P<0.01), although salt used for seasoning was not assessed. The distributions of traffic light colours under the FSA's food labelling recommendations differed: the modal traffic light was red for the recipes (47%) and green for ready meals (42%). Overall, the recipes contained significantly more energy (2530 kJ v 2067 kJ), protein (37.5 g v 27.9 g), fat (27.1 g v 17.2 g), and saturated fat (9.2 g v 6.8 g; P<0.01 for all) and significantly less fibre (3.3 g v 6.5 g, P<0.01) per portion than the ready meals.
>
>
>CONCLUSIONS
>Neither recipes created by television chefs nor ready meals sold by three of the leading UK supermarkets complied with WHO recommendations. Recipes were less healthy than ready meals, containing significantly more energy, protein, fat, and saturated fat, and less fibre per portion than the ready meals.

<details>
<summary>Notes</summary>

#### Summary
This article compares chef and ready meals recipes.

#### Limitations
- The analysis has been done on only 5 chef books which were top saled, this might be a biased view of chef recipe.
- A significance test of the proportion size would be interesting to evaluate if books tend to have bigger size.

#### Tags
[\#Cuisine](#Cuisine) [\#Eating](#Eating) [\#England](#England) [\#Grocery](#Grocery) 
</details>

### <a name='4'></a> \[4\] [The Spread of Obesity in a Large Social Network over 32 Years](https://doi.org/10.1056/NEJMsa066082) 

by Christakis, Nicholas A. and Fowler, James H.
 in 2007

#### Abstract
> BACKGROUND
>The prevalence of obesity has increased substantially over the past 30 years. We performed a quantitative analysis of the nature and extent of the person-to-person spread of obesity as a possible factor contributing to the obesity epidemic.
>
>METHODS
>We evaluated a densely interconnected social network of 12,067 people assessed repeatedly from 1971 to 2003 as part of the Framingham Heart Study. The body-mass index was available for all subjects. We used longitudinal statistical models to examine whether weight gain in one person was associated with weight gain in his or her friends, siblings, spouse, and neighbors.
>
>RESULTS
>Discernible clusters of obese persons (body-mass index [the weight in kilograms divided by the square of the height in meters], >=30) were present in the network at all time points, and the clusters extended to three degrees of separation. These clusters did not appear to be solely attributable to the selective formation of social ties among obese persons. A person's chances of becoming obese increased by 57% (95% confidence interval [CI], 6 to 123) if he or she had a friend who became obese in a given interval. Among pairs of adult siblings, if one sibling became obese, the chance that the other would become obese increased by 40% (95% CI, 21 to 60). If one spouse became obese, the likelihood that the other spouse would become obese increased by 37% (95% CI, 7 to 73). These effects were not seen among neighbors in the immediate geographic location. Persons of the same sex had relatively greater influence on each other than those of the opposite sex. The spread of smoking cessation did not account for the spread of obesity in the network.
>
>CONCLUSIONS
>Network phenomena appear to be relevant to the biologic and behavioral trait of obesity, and obesity appears to spread through social ties. These findings have implications for clinical and public health interventions.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the spread of obesity through the relations network.

#### Conclusions
- Significant increase of obesity if friends or siblings became obese (3 degree)
- Social link more important than geographical distance

#### Limitations
- Is there a selection bias from the population selected (only from Framingham Offspring Study - How have they been chosen ? Location, Class ...)
- Is there an impact if people are more obses (not taking obese as a binary but take the value of BMI into account)
- Is the density of the network impacting the gain of weight ?
- Is the opposite also true ?

#### Tags
[\#Obesity](#Obesity) [\#Network](#Network) [\#USA](#USA) 
</details>

### <a name='5'></a> \[5\] [Income disparities in body mass index and obesity in the United States, 1971-2002](https://www.ncbi.nlm.nih.gov/pubmed/16217002) 

by Chang, Virginia W and Lauderdale, Diane S
 in 2005

#### Abstract
> BACKGROUND:
>Although obesity is frequently associated with poverty, recent increases in obesity may not occur disproportionately among the poor. Furthermore, the relationship between income and weight status may be changing with time.
>
>METHODS:
>We use nationally representative data from the National Health and Nutrition Examination Surveys (1971-2002) to examine (1) income differentials in body mass index (calculated as weight in kilograms divided by the square of height in meters) and (2) change over time in the prevalence of obesity (body mass index, >or=30) at different levels of income.
>
>RESULTS:
>Over the course of 3 decades, obesity has increased at all levels of income. Moreover, it is typically not the poor who have experienced the largest gains. For example, among black women, the absolute increase in obesity is 27.0% (1.05% per year) for those at middle incomes, but only 14.5% (0.54% per year) for the poor. Among black men, the increase in obesity is 21.1% (0.77% per year) for those at the highest level of income, but only 4.5% (0.06% per year) for the near poor and 5.4% (0.50% per year) for the poor. Furthermore, all race-sex groups show income differentials on body mass index, but patterns show substantial variation between groups and consistency and change within groups over time. For example, white women consistently show a strong inverse gradient, while a positive gradient emerges in later waves for black and Mexican American men.
>
>CONCLUSION:
>The persistence and emergence of income gradients suggests that disparities in weight status are only partially attributable to poverty and that efforts aimed at reducing disparities need to consider a much broader array of contributing factors.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the evolution of obesity and BMI from 1971 to 2002 given sex, racial and poverty information.

#### Conclusions
- Significant increase of obesity overall
- Gender and races impacts the evolution (women have a negative gradient between income and IBM, more or less significant given race; black men have a strong positive gradient, where other men have non significant trends)
- Obesity is not consistently higher in the poor
- Sex and race impacts suggest that income is not the only factor impacting weight

#### Limitations
- A measure of correlation through time could avoid to stratified in three different periods of time.

#### Tags
[\#Obesity](#Obesity) [\#Poverty](#Poverty) [\#USA](#USA) 
</details>

### <a name='6'></a> \[6\] [Exploiting food choice biases for healthier recipe recommendation](https://dl.acm.org/citation.cfm?id=3080826) 

by Elsweiler, David and Trattner, Christoph and Harvey, Morgan
 in 2017

#### Abstract
> By incorporating healthiness into the food recommendation / ranking process we have the potential to improve the eating habits of a growing number of people who use the Internet as a source of food inspiration. In this paper, using insights gained from various data sources, we explore the feasibility of substituting meals that would typically be recommended to users with similar, healthier dishes. First, by analysing a recipe collection sourced from Allrecipes.com, we quantify the potential for finding replacement recipes, which are comparable but have different nutritional characteristics and are nevertheless highly rated by users. Building on this, we present two controlled user studies (n=107, n=111) investigating how people perceive and select recipes. We show participants are unable to reliably identify which recipe contains most fat due to their answers being biased by lack of information, misleading cues and limited nutritional knowledge on their part. By applying machine learning techniques to predict the preferred recipes, good performance can be achieved using low-level image features and recipe meta-data as predictors. Despite not being able to consciously determine which of two recipes contains most fat, on average, participants select the recipe with the most fat as their preference. The importance of image features reveals that recipe choices are often visually driven. A final user study (n=138) investigates to what extent the predictive models can be used to select recipe replacements such that users can be ``nudged'' towards choosing healthier recipes. Our findings have important implications for online food systems.

<details>
<summary>Notes</summary>

#### Summary
This article proposes approached to show in a food recommender system similar recipes with less fat options.

#### Conclusions
- Users have a hard time to guess from images which recipe is less fat.
- Users tends to prefer nicer images
- Users are impacted by popularity

#### Limitations
- Definition of healthy as fat content is biased
- Fat per serving is also a bad idea in the sense that serving is badly defined (a caloric density would be better)
- Taking also the fiber density would be great
- Influencing the choice by enhancing the images (as Netflix does) would be an interesting point to nudge people towards healthier recipes

#### Tags
[\#Cuisine](#Cuisine) [\#Eating](#Eating) [\#Recommender](#Recommender) 
</details>

### <a name='7'></a> \[7\] [Health-aware food recommender system](https://dl.acm.org/citation.cfm?id=2796554) 

by Ge, Mouzhi and Ricci, Francesco and Massimo, David
 in 2015

#### Abstract
> With the rapid changes in the food variety and lifestyles, many people are facing the problem of making healthier food decisions to reduce the risk of chronic diseases such as obesity and diabetes. To this end, our recommender system not only offers recipe recommendations that suit the user's preference but is also able to take the user's health into account. It is developed on a mobile platform by considering that our application may be directly used in the kitchen. This demo paper summarizes the complete human-computer interaction design, the implemented health-aware recommendation algorithm and preliminary user feedback.

<details>
<summary>Notes</summary>

#### Summary
This article proposes a food recommender system that takes into account the calories needed by the user and the calories from the recipe.

#### Limitations
- Measure of healthiness should not relie on calories.

#### Tags
[\#Cuisine](#Cuisine) [\#Eating](#Eating) [\#Recommender](#Recommender) 
</details>

### <a name='8'></a> \[8\] [\# foodporn: Obesity patterns in culinary interactions](https://arxiv.org/abs/1503.01546) 

by Mejova, Yelena and Haddadi, Hamed and Noulas, Anastasios and Weber, Ingmar
 in 2015

#### Abstract
> We present a large-scale analysis of Instagram pictures taken at 164,753 restaurants by millions of users. Motivated by the obesity epidemic in the United States, our aim is three-fold: (i) to assess the relationship between fast food and chain restaurants and obesity, (ii) to better understand people's thoughts on and perceptions of their daily dining experiences, and (iii) to reveal the nature of social reinforcement and approval in the context of dietary health on social media. When we correlate the prominence of fast food restaurants in US counties with obesity, we find the Foursquare data to show a greater correlation at 0.424 than official survey data from the County Health Rankings would show. Our analysis further reveals a relationship between small businesses and local foods with better dietary health, with such restaurants getting more attention in areas of lower obesity. However, even in such areas, social approval favors the unhealthy foods high in sugar, with donut shops producing the most liked photos. Thus, the dietary landscape our study reveals is a complex ecosystem, with fast food playing a role alongside social interactions and personal perceptions, which often may be at odds.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the relationship beteen the number of fast food restaurants and the obesity level in US counties.

#### Conclusions
- Strong correlation

#### Limitations
- Make link between number of comment and social approval without regard to the population size of those counties (it is shown that more obese areas have less comment and likes)
- An interesting remark is that social network is a bias selection in the sense that mainly young and tech oriented perople will tend to use it (also people tends to show only what they consider positive)
- It would be interesting to split the emotioin category associated to the comment into postive and negative

#### Tags
[\#Obesity](#Obesity) [\#Social Network](#Social_Network) [\#USA](#USA) 
</details>

### <a name='9'></a> \[9\] [Impact of front-of-pack 'traffic-light' nutrition labelling on consumer food purchases in the UK](https://academic.oup.com/heapro/article/24/4/344/575241) 

by Sacks, Gary and Rayner, Mike and Swinburn, Boyd
 in 2009

#### Abstract
> Front-of-pack 'traffic-light' nutrition labelling has been widely proposed as a tool to improve public health nutrition. This study examined changes to consumer food purchases after the introduction of traffic-light labels with the aim of assessing the impact of the labels on the 'healthiness' of foods purchased. The study examined sales data from a major UK retailer in 2007. We analysed products in two categories ('ready meals' and sandwiches), investigating the percentage change in sales 4 weeks before and after traffic-light labels were introduced, and taking into account seasonality, product promotions and product life-cycle. We investigated whether changes in sales were related to the healthiness of products. All products that were not new and not on promotion immediately before or after the introduction of traffic-light labels were selected for the analysis (n = 6 for ready meals and n = 12 for sandwiches). For the selected ready-meals, sales increased (by 2.4% of category sales) in the 4 weeks after the introduction of traffic-light labels, whereas sales of the selected sandwiches did not change significantly. Critically, there was no association between changes in product sales and the healthiness of the products. This short-term study based on a small number of ready meals and sandwiches found that the introduction of a system of four traffic-light labels had no discernable effect on the relative healthiness of consumer purchases. Further research on the influence of nutrition signposting will be needed before this labelling format can be considered a promising public health intervention.

<details>
<summary>Notes</summary>

#### Summary
This article analyzes the impact of the tri color signal on food package on the healthiness of purchase.

#### Conclusions
People were not impacted by this change in the 8 weeks around this time

#### Limitations
- Impact of the media speaking about this change had perhaps increased the attention and the change wouldn't have been observed at that time
- A meta analysis would be more interesting to see if the global healthiness have changed

#### Tags
[\#Eating](#Eating) [\#Recommender](#Recommender) [\#England](#England) [\#Grocery](#Grocery) 
</details>

### <a name='10'></a> \[10\] [Is everything we eat associated with cancer? A systematic cookbook review](https://europepmc.org/abstract/med/23193004) 

by Schoenfeld, Jonathan D and Ioannidis, John PA
 in 2012

#### Abstract
> BACKGROUND: Nutritional epidemiology is a highly prolific field. Debates on associations of nutrients with disease risk are common in the literature and attract attention in public media. OBJECTIVE: We aimed to examine the conclusions, statistical significance, and reproducibility in the literature on associations between specific foods and cancer risk. DESIGN: We selected 50 common ingredients from random recipes in a cookbook. PubMed queries identified recent studies that evaluated the relation of each ingredient to cancer risk. Information regarding author conclusions and relevant effect estimates were extracted. When >10 articles were found, we focused on the 10 most recent articles. RESULTS: Forty ingredients (80%) had articles reporting on their cancer risk. Of 264 single-study assessments, 191 (72%) concluded that the tested food was associated with an increased (n = 103) or a decreased (n = 88) risk; 75% of the risk estimates had weak (0.05 > P >= 0.001) or no statistical (P > 0.05) significance. Statistically significant results were more likely than nonsignificant findings to be published in the study abstract than in only the full text (P < 0.0001). Meta-analyses (n = 36) presented more conservative results; only 13 (26%) reported an increased (n = 4) or a decreased (n = 9) risk (6 had more than weak statistical support). The median RRs (IQRs) for studies that concluded an increased or a decreased risk were 2.20 (1.60, 3.44) and 0.52 (0.39, 0.66), respectively. The RRs from the meta-analyses were on average null (median: 0.96; IQR: 0.85, 1.10). CONCLUSIONS: Associations with cancer risk or benefits have been claimed for most food ingredients. Many single studies highlight implausibly large effects, even though evidence is weak. Effect sizes shrink in meta-analyses.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the disease risk asxociated to different ingredients given the literature.

#### Conclusions
- All food was related to an increased cancer risk.
- Pressure for publication forces publication of weakly significant result and overinterpretation of results.

#### Limitations
Finer meta analysis could identify which studies have more weight

#### Tags
[\#Eating](#Eating) [\#Cancer](#Cancer) [\#Meta Analysis](#Meta_Analysis) 
</details>

### <a name='11'></a> \[11\] [You are What you Eat (and Drink): Identifying Cultural Boundaries by Analyzing Food & Drink Habits in Foursquare](https://arxiv.org/abs/1404.1009) 

by Thiago H Silva and Pedro O S Vaz de Melo and Jussara Almeida and Mirco Musolesi and Antonio Loureiro
 in 2014

#### Abstract
> Food and drink are two of the most basic needs of human beings. However, as society evolved, food and drink became also a strong cultural aspect, being able to describe strong differences among people. Traditional methods used to analyze cross-cultural differences are mainly based on surveys and, for this reason, they are very difficult to represent a significant statistical sample at a global scale. In this paper, we propose a new methodology to identify cultural boundaries and similarities across populations at different scales based on the analysis of Foursquare check-ins. This approach might be useful not only for economic purposes, but also to support existing and novel marketing and social applications. Our methodology consists of the following steps. First, we map food and drink related check-ins extracted from Foursquare into users' cultural preferences. Second, we identify particular individual preferences, such as the taste for a certain type of food or drink, e.g., pizza or sake, as well as temporal habits, such as the time and day of the week when an individual goes to a restaurant or a bar. Third, we show how to analyze this information to assess the cultural distance between two countries, cities or even areas of a city. Fourth, we apply a simple clustering technique, using this cultural distance measure, to draw cultural boundaries across countries, cities and regions.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the food habits by analyzing social network. It looks at user similarity, region similarity and anlyze temporal patterns.

#### Conclusions
Cultural differences can be observed using food related information.

#### Limitations
- Limits of social network reflecting a subpart od the population.
- More demographics about users should be gathered

#### Tags
[\#Eating](#Eating) [\#Social Network](#Social_Network) 
</details>

### <a name='12'></a> \[12\] [Investigating the healthiness of internet-sourced recipes: implications for meal planning and recommender systems](https://dl.acm.org/citation.cfm?id=3052573) 

by Trattner, Christoph and Elsweiler, David
 in 2017

#### Abstract
> Food recommenders have the potential to positively influence the eating habits of users. To achieve this, however, we need to understand how healthy recommendations are and the factors which influence this. Focusing on two approaches from the literature (single item and daily meal plan recommendation) and utilizing a large Internet sourced dataset from Allrecipes.com, we show how algorithmic solutions relate to the healthiness of the underlying recipe collection. First, we analyze the healthiness of Allrecipes.com recipes using nutritional standards from the World Health Organisation and the United Kingdom Food Standards Agency. Second, we investigate user interaction patterns and how these relate to the healthiness of recipes. Third, we experiment with both recommendation approaches. Our results indicate that overall the recipes in the collection are quite unhealthy, but this varies across categories on the website. Users in general tend to interact most often with the least healthy recipes. Recommender algorithms tend to score popular items highly and thus on average promote unhealthy items. This can be tempered, however, with simple post-filtering approaches, which we show by experiment are better suited to some algorithms than others. Similarly, we show that the generation of meal plans can dramatically increase the number of healthy options open to users. One of the main findings is, nevertheless, that the utility of both approaches is strongly restricted by the recipe collection. Based on our findings we draw conclusions how researchers should attempt to make food recommendation systems promote healthy nutrition.

<details>
<summary>Notes</summary>

#### Summary
This article analyses the recipes from AllRecipes from a helthiness point of view. It also shows the preferences of user and how to adapt the recommendations to encourage healthy eating.

#### Conclusions
Users prefer unhealthy recipes. Recommender should weight their recommendations given the health index.

#### Limitations
- Study done on AllRecipes which is used mainly by Americans, are the conclusions generalizable ?
- Healthiness is defined by the standard convention (which has changed a lot during the past year), an adaptable definition would be more interesting: how to integrate microbiome studies to make adapted recommender systems ?
- Are the likes and comments a real reflect of what people consumes ?

#### Tags
[\#Eating](#Eating) [\#Recommender](#Recommender) [\#Social Network](#Social_Network) [\#USA](#USA) 
</details>

### <a name='13'></a> \[13\] [An obesity-associated gut microbiome with increased capacity for energy harvest](https://www.nature.com/articles/nature05414/) 

by Turnbaugh, Peter J and Ley, Ruth E and Mahowald, Michael A and Magrini, Vincent and Mardis, Elaine R and Gordon, Jeffrey I
 in 2006

#### Abstract
> The worldwide obesity epidemic is stimulating efforts to identify host and environmental factors that affect energy balance. Comparisons of the distal gut microbiota of genetically obese mice and their lean littermates, as well as those of obese and lean human volunteers have revealed that obesity is associated with changes in the relative abundance of the two dominant bacterial divisions, the Bacteroidetes and the Firmicutes. Here we demonstrate through metagenomic and biochemical analyses that these changes affect the metabolic potential of the mouse gut microbiota. Our results indicate that the obese microbiome has an increased capacity to harvest energy from the diet. Furthermore, this trait is transmissible: colonization of germ-free mice with an 'obese microbiota' results in a significantly greater increase in total body fat than colonization with a 'lean microbiota'. These results identify the gut microbiota as an additional contributing factor to the pathophysiology of obesity.

<details>
<summary>Notes</summary>

#### Summary
This article shows the impact of microbiome composition on calories absorption.

#### Conclusions
Obese microbiome has an increased capacity for energy harvest from similar diet.

#### Limitations
- Study done on 8 mice on a period of 14 days. Is the microbiome adapting on a longer period of time ?
- Are those results appliable to humans ?
- What would originally create this difference in microbiome ?

#### Tags
[\#Obesity](#Obesity) [\#Mircrobiome](#Mircrobiome) 
</details>

### <a name='14'></a> \[14\] [Neurobiologic basis of craving for carbohydrates](https://www.ncbi.nlm.nih.gov/pubmed/24139726) 

by Ventura, Tamara and Santander, Jaime and Torres, Rafael and Contreras, Ana Mar{\'\i}a
 in 2014

#### Abstract
> OBJECTIVES:
>There is a relationship between emotional disorders, obesity, and craving for carbohydrates. This relationship complicates the success of treatments aimed at combatting obesity, which is considered to be the epidemic of the twenty-first century. We conducted a review of the neurobiologic basis for carbohydrate craving, with the hope that this understanding will enable the design of more efficient therapeutic strategies.
>
>METHOD:
>We conducted a non-systematic literature search in PubMed using MeSH.
>
>RESULTS:
>Research on the basis of carbohydrate craving is varied, but may be grouped into five main areas: the serotonergic system, palatability and hedonic response, the motivational system, stress response systems, and gene-environment interaction.
>
>CONCLUSIONS:
>The models that integrate motivational systems with palatability and hedonic response studies are the ones that we believe can best explain both craving for carbohydrates and related addictive phenomena. Research has contributed to a greater understanding of the neurobiologic basis of carbohydrate craving. The latter, in turn, contributes to an understanding of the implications, challenges, and possible therapies that might be put in place to cope with this phenomenon.

<details>
<summary>Notes</summary>

#### Summary
This article reviews different explanations for carbs craving.

#### Conclusions
- Serotoninc: Carbo => Increase Trp => Increase Serotonine => Happier. If true, could be corrected by using serotonine related medications (rejected because observed effect is direct and the process involving serotonine should be slower)
- Palatability and hedonic response: Perception of sweet taste implies an opioid response. Could be corrected by drugs on opioid receptor
- Motivational system: Imporves mood by dopamine increase but can lead to a dependence. Should be treated as a drug
- Stress response: Reduce stress
- Gene environment: Behavior learnt from inadequate parenting or inability to distinguish hunger from other internal states.

#### Limitations
- No microbiome analysis is reviewed

#### Tags
[\#Neurobio](#Neurobio) [\#Portion](#Portion) [\#Eating](#Eating) 
</details>

### <a name='15'></a> \[15\] [Ice cream illusions: bowls, spoons, and self-served portion sizes](https://www.ncbi.nlm.nih.gov/pubmed/16905035) 

by Wansink, Brian and Van Ittersum, Koert and Painter, James E
 in 2006

#### Abstract
> BACKGROUND:
>Because people eat most of what they serve themselves, any contextual cues that lead them to over-serve should lead them to over-eat. In building on the size-contrast illusion, this research examines whether the size of a bowl or serving spoon unknowingly biases how much a person serves and eats.    
>
>METHODS:
>The 2 x 2 between-subjects design involved 85 nutrition experts who were attending an ice cream social to celebrate the success of a colleague in 2002. They were randomly given either a smaller (17 oz) or a larger (34 oz) bowl and either a smaller (2 oz) or larger (3 oz) ice cream scoop. After serving themselves, they completed a brief survey as their ice cream was weighed. The analysis was conducted in 2003.
>
>RESULTS:
>Even when nutrition experts were given a larger bowl, they served themselves 31.0% more (6.25 vs 4.77 oz, F(1, 80) = 8.05, p < 0.01) without being aware of it. Their servings increased by 14.5% when they were given a larger serving spoon (5.77 vs 5.04 oz, F(1, 80)=2.70, p = 0.10).
>
>CONCLUSIONS:
>People could try using the size of their bowls and possibly serving spoons to help them better control how much they consume. Those interested in losing weight should use smaller bowls and spoons, while those needing to gain weight--such as the undernourished or aged--could be encouraged to use larger ones. Epidemiologic implications are discussed.

<details>
<summary>Notes</summary>

#### Summary
This article shows the impact of plate and ustensils size on the food consumption.

#### Conclusions
- Larger is the plate, more people eat
- People are not aware of this difference of portion size
- Calorie concentration is more important than calorie consumption

#### Limitations
- Does it depend of the population ?
- Is the impact opposite for anorexic or obese patients ?

#### Tags
[\#Obesity](#Obesity) [\#Portion](#Portion) [\#Eating](#Eating) [\#USA](#USA) 
</details>

### <a name='16'></a> \[16\] [Crowdsourcing health labels: Inferring body weight from profile pictures](https://dl.acm.org/citation.cfm?id=2897727) 

by Weber, Ingmar and Mejova, Yelena
 in 2016

#### Abstract
> To use social media for health-related analysis, one key step is the detection of health-related labels for users. But unlike transient conditions like flu, social media users are less vocal about chronic conditions such as obesity, as users might not tweet ``I'm still overweight''. As, however, obesity-related conditions such as diabetes, heart disease, osteoarthritis, and even cancer are on the rise, this obese-or-not label could be one of the most useful for studies in public health.
>In this paper we investigate the feasibility of using profile pictures to infer if a user is overweight or not. We show that this is indeed possible and further show that the fraction of labeled-as-overweight users is higher in U.S. counties with higher obesity rates. Going from public to individual health analysis, we then find differences both in behavior and social networks, for example finding users labeled as overweight to have fewer followers.

<details>
<summary>Notes</summary>

#### Summary
This article asks a crowdsource to evaluate if twitter users are overweighted based on their profile picture.

#### Limitations
- No ground truth
- Only 3 persons who evaluates and conclusion made on their consensus correlated to the number of obese in different counties
- Models should be built to predict the label obtained
- Vocabulary used in the tweet should be studied in a discriminative fashiion, to evaluate what is characteristic of each group.

#### Tags
[\#Obesity](#Obesity) [\#Social Network](#Social_Network) [\#CrowdSource](#CrowdSource) 
</details>

### <a name='17'></a> \[17\] [Personalized nutrition by prediction of glycemic responses](https://www.cell.com/cell/fulltext/S0092-8674(15)01481-6#) 

by Zeevi, David and Korem, Tal and Zmora, Niv and Israeli, David and Rothschild, Daphna and Weinberger, Adina and Ben-Yacov, Orly and Lador, Dar and Avnit-Sagi, Tali and Lotan-Pompan, Maya and others
 in 2015

#### Abstract
> Elevated postprandial blood glucose levels constitute a global epidemic and a major risk factor for prediabetes and type II diabetes, but existing dietary methods for controlling them have limited efficacy. Here, we continuously monitored week-long glucose levels in an 800-person cohort, measured responses to 46,898 meals, and found high variability in the response to identical meals, suggesting that universal dietary recommendations may have limited utility. We devised a machine-learning algorithm that integrates blood parameters, dietary habits, anthropometrics, physical activity, and gut microbiota measured in this cohort and showed that it accurately predicts personalized postprandial glycemic response to real-life meals. We validated these predictions in an independent 100-person cohort. Finally, a blinded randomized controlled dietary intervention based on this algorithm resulted in significantly lower postprandial responses and consistent alterations to gut microbiota configuration. Together, our results suggest that personalized diets may successfully modify elevated postprandial blood glucose and its metabolic consequences.

<details>
<summary>Notes</summary>

#### Summary
Measures the blood sugar response to identical meals

#### Conclusions
- Response varies greatly from one user to another
- Gradient boosting regression allows to predict the response given microbiome and different information concerning the user much better than model built on carbohydrate content only
- High agreement between multiple intake of the same food for one individual
- Carb sensitivity is patient specific
- Nutrition impact significantly the microbiome population of the host

#### Limitations
- An analysis using only microbiome would be interesting to remove interaction between features
-  Why 2 hours after meal have been considered ?
- PDP chosen for showing impact of features: it assumes independence of features ...

#### Tags
[\#Mircrobiome](#Mircrobiome) [\#ML](#ML) [\#Eating](#Eating) 
</details>

### <a name='18'></a> \[18\] [Geography and similarity of regional cuisines in China](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079161) 

by Zhu, Yu-Xiao and Huang, Junming and Zhang, Zi-Ke and Zhang, Qian-Ming and Zhou, Tao and Ahn, Yong-Yeol
 in 2013

#### Abstract
> Food occupies a central position in every culture and it is therefore of great interest to understand the evolution of food culture. The advent of the World Wide Web and online recipe repositories have begun to provide unprecedented opportunities for data-driven, quantitative study of food culture. Here we harness an online database documenting recipes from various Chinese regional cuisines and investigate the similarity of regional cuisines in terms of geography and climate. We find that geographical proximity, rather than climate proximity, is a crucial factor that determines the similarity of regional cuisines. We develop a model of regional cuisine evolution that provides helpful clues for understanding the evolution of cuisines and cultures.

<details>
<summary>Notes</summary>

#### Summary
This article analyzes the impact of geography and climate proximity on food similarity.

#### Conclusions
- Geogrphic proximity important in proximity more than climate proximity
- Outliers explained by historical reasons

#### Limitations
- Conclusions linked to climate sound limited because only look at difference of mean temperature of the capitals

#### Tags
[\#Cuisine](#Cuisine) [\#Geography](#Geography) [\#China](#China) 
</details>


## Tags

#### <a name='Cancer'></a> Cancer

[\[10\]](#10)
#### <a name='China'></a> China

[\[18\]](#18)
#### <a name='CrowdSource'></a> CrowdSource

[\[16\]](#16)
#### <a name='Cuisine'></a> Cuisine

[\[3\]](#3), [\[6\]](#6), [\[7\]](#7), [\[18\]](#18)
#### <a name='Eating'></a> Eating

[\[3\]](#3), [\[6\]](#6), [\[7\]](#7), [\[9\]](#9), [\[10\]](#10), [\[11\]](#11), [\[12\]](#12), [\[14\]](#14), [\[15\]](#15), [\[17\]](#17)
#### <a name='England'></a> England

[\[2\]](#2), [\[3\]](#3), [\[9\]](#9)
#### <a name='Geography'></a> Geography

[\[18\]](#18)
#### <a name='Grocery'></a> Grocery

[\[2\]](#2), [\[3\]](#3), [\[9\]](#9)
#### <a name='ML'></a> ML

[\[2\]](#2), [\[17\]](#17)
#### <a name='Meta_Analysis'></a> Meta Analysis

[\[10\]](#10)
#### <a name='Mircrobiome'></a> Mircrobiome

[\[13\]](#13), [\[17\]](#17)
#### <a name='Network'></a> Network

[\[1\]](#1), [\[4\]](#4)
#### <a name='Neurobio'></a> Neurobio

[\[14\]](#14)
#### <a name='Obesity'></a> Obesity

[\[1\]](#1), [\[2\]](#2), [\[4\]](#4), [\[5\]](#5), [\[8\]](#8), [\[13\]](#13), [\[15\]](#15), [\[16\]](#16)
#### <a name='Portion'></a> Portion

[\[14\]](#14), [\[15\]](#15)
#### <a name='Poverty'></a> Poverty

[\[5\]](#5)
#### <a name='Recommender'></a> Recommender

[\[6\]](#6), [\[7\]](#7), [\[9\]](#9), [\[12\]](#12)
#### <a name='Social_Network'></a> Social Network

[\[1\]](#1), [\[8\]](#8), [\[11\]](#11), [\[12\]](#12), [\[16\]](#16)
#### <a name='USA'></a> USA

[\[1\]](#1), [\[4\]](#4), [\[5\]](#5), [\[8\]](#8), [\[12\]](#12), [\[15\]](#15)
