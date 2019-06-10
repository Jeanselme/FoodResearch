# [Food Realted Research](https://jeanselme.github.io/FoodResearch/)

## Articles

### <a name='1'></a> \[1\] [Large-scale and high-resolution analysis of food purchases and health outcomes](https://doi.org/10.1140/epjds/s13688-019-0191-y) 

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

### <a name='2'></a> \[2\] [The Spread of Obesity in a Large Social Network over 32 Years](https://doi.org/10.1056/NEJMsa066082) 

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

### <a name='3'></a> \[3\] [Income disparities in body mass index and obesity in the United States, 1971-2002](https://www.ncbi.nlm.nih.gov/pubmed/16217002) 

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

### <a name='4'></a> \[4\] [\# foodporn: Obesity patterns in culinary interactions](https://arxiv.org/abs/1503.01546) 

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
[\#Obesity](#Obesity) [\#Social Network](#Social Network) [\#USA](#USA) 
</details>

### <a name='5'></a> \[5\] [An obesity-associated gut microbiome with increased capacity for energy harvest](https://www.nature.com/articles/nature05414/) 

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

### <a name='6'></a> \[6\] [Ice cream illusions: bowls, spoons, and self-served portion sizes](https://www.ncbi.nlm.nih.gov/pubmed/16905035) 

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

### <a name='7'></a> \[7\] [Crowdsourcing health labels: Inferring body weight from profile pictures](https://dl.acm.org/citation.cfm?id=2897727) 

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
[\#Obesity](#Obesity) [\#Social Network](#Social Network) [\#CrowdSource](#CrowdSource) 
</details>


## Tags

#### <a name='CrowdSource'></a> CrowdSource

[\[7\]](#7)
#### <a name='Eating'></a> Eating

[\[6\]](#6)
#### <a name='England'></a> England

[\[1\]](#1)
#### <a name='Grocery'></a> Grocery

[\[1\]](#1)
#### <a name='ML'></a> ML

[\[1\]](#1)
#### <a name='Mircrobiome'></a> Mircrobiome

[\[5\]](#5)
#### <a name='Network'></a> Network

[\[2\]](#2)
#### <a name='Obesity'></a> Obesity

[\[1\]](#1), [\[2\]](#2), [\[3\]](#3), [\[4\]](#4), [\[5\]](#5), [\[6\]](#6), [\[7\]](#7)
#### <a name='Portion'></a> Portion

[\[6\]](#6)
#### <a name='Poverty'></a> Poverty

[\[3\]](#3)
#### <a name='Social Network'></a> Social Network

[\[4\]](#4), [\[7\]](#7)
#### <a name='USA'></a> USA

[\[2\]](#2), [\[3\]](#3), [\[4\]](#4), [\[6\]](#6)
