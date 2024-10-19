# Machine Learning II

Created: October 5, 2024 1:16 PM
Tags: Association

# Session 1 : Association Analysis

<aside>
💾

[Zoom Recording]

</aside>

<aside>
🔖

Additional Documentation : 



</aside>

<aside>
📢

**Key Takeaways**

- The goal of association analysis is to ***find rules from a business perspective.***
- No inference is happening, but we’re rather interested in ***correlation**.*
- We will **generate rules** explaining those correlations and we’ll need to filter them.
- We need **data in tabular format** to find rules and do predictions.
- The measurement to filter the rules are,
    - **Support**  = *antecedents / total*
    - **Rule Support** =  *support * confidence*
    - **Posterior Confidence** = *(antecedents and consequent at the same time) / instances*
    - **Prior confidence / Consequent Support** = support for the consequent
    - **Lift** = *posterior confidence / prior confidence* > the higher the better
        - We will use it to filter out the rules, ex. we’ll add a threshold and we’ll select ONLY the rules with a lift > X
    - **Confidence difference** = *| posterior confidence - prior confidence |*
        - We will ALSO add a threshold in this measurement, it will be used for negative rules, AKA when PRIOR confidence is higher than POSTERIOR one
    - **Confidence ratio** =  *1 - (min(post,prior)/max(post,prior))*
</aside>

Recommended books

![Screenshot 2024-10-05 at 13.16.18.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.16.18.png)

![Screenshot 2024-10-05 at 13.17.34.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.17.34.png)

Is also called **market basket analysis.** Is about finding events happening together frequently. The goal is to ***find rules from a business perspective.*** For example if a person gets diapers they will also get beer. **

Correlation is NOT equals to causation. We are now interested in **CORRELATION**, because we think an event that happened, may happen again in the future. We not dealing with stats now, no inference is happening.

Some examples of those events > *if you are overweight you might have high blood pressure*

An application of this technique is predictive maintenance, fraud, etc

A **RULE** would look like that

![Screenshot 2024-10-05 at 13.24.40.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.24.40.png)

if you bought bread and butter, you’ll buy milk

![Screenshot 2024-10-10 at 12.17.21.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_12.17.21.png)

![Screenshot 2024-10-05 at 13.25.08.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.25.08.png)

We have a problem, a number of rules for a given item grows exponentially. So we need to find a way of reduce the # of rules! 

![Screenshot 2024-10-05 at 13.26.27.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.26.27.png)

**Cutting down the amount of rules by using some criteria**

How frequent are this items?

![Screenshot 2024-10-05 at 13.27.07.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.27.07.png)

How likely is this rule to happen?

![Screenshot 2024-10-05 at 13.27.27.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.27.27.png)

## Filtering Rules out : Measurements to select rules

**Rule >** If they buy fuel & chocolate > they’ll buy newspapers

![Screenshot 2024-10-10 at 12.19.44.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_12.19.44.png)

![Screenshot 2024-10-05 at 13.32.41.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.32.41.png)

Support = fuel + choco / total items = *antecedents / total*

Confidence = (fuel + choco + newspaper) / (fuel + choco) = *(antecedents and consequent at the same time) / instances*

Rule Support = (fuel + choco + newspaper) / total items = *support * confidence*

<aside>
💡

*We introduce measurements for this,*

- **Support**  =*antecedents / total*
- **Confidence** = *(antecedents and consequent at the same time) / instances*
- **Rule Support** =  *support * confidence*
</aside>

These measurements ( Support, Confidence,…) are not fully reliable so we bring the following ones, 

![Screenshot 2024-10-05 at 13.36.07.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.36.07.png)

<aside>
💡

- **Posterior Confidence** is like Confidence > *(antecedents and consequent at the same time) / instances for the RULE*
- **Prior confidence** > support for the consequent, ex. only for newspapers
</aside>

<aside>
💡

*We compare both to see on what % the posterior is increased! We’ll introduce new measurements for this,*

- **Lift** = *posterior confidence / prior confidence* > the higher the better
    - We will use it to filter out the rules, ex. we’ll add a threshold and we’ll select ONLY the rules with a lift > X
- **Confidence difference** = *| posterior confidence - prior confidence |*
    - We will ALSO add a threshold in this measurement, it will be used for negative rules, AKA when PRIOR confidence is higher than POSTERIOR one
- **Confidence ratio** =  *1 - (min(post,prior)/max(post,prior))*
</aside>

Example - same as before

![Screenshot 2024-10-05 at 13.48.58.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.48.58.png)

## Data formats : How do we treat data ?

We can have transactional or tabular data. Aka, tabular is when every row is a customer and the columns are variables. Transactional on the other side, it has 2 columns, there’s a row per transaction.

<aside>
💡

![Screenshot 2024-10-10 at 12.58.06.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_12.58.06.png)

</aside>

![Screenshot 2024-10-10 at 12.59.00.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_12.59.00.png)

We can also have raw data, but the algorithm ***ONLY works with transactional or tabular data***

![Screenshot 2024-10-05 at 13.52.06.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.52.06.png)

![Screenshot 2024-10-05 at 13.51.57.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-05_at_13.51.57.png)

For every customer will find the set of rules that best apply to them aka, the one with the highest confidence, for which we can make predictions. To find the confidence we need the data to be Tabular so it’s the most preferred one, because we can add predictions.

## **Example in Dataiku**

What we did in class step by step:

- Create a dataset
- Within the dataset, select the MEAN. It shows the % of people that bought each of the items.
    
    ![Screenshot 2024-10-10 at 13.19.04.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_13.19.04.png)
    
- Upload the Python workbook - Apriori -  provided in the forum.
- ❗ Beware - dataiku.dataset(<Dataset Name>) needs to be revised and changed with the name given to our dataset.
- Decide which metric I’ll be using and its threshold and set them in the notebook
    
    ![Screenshot 2024-10-10 at 13.25.55.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_13.25.55.png)
    

- The results of the execution is the following, - *It contains all the variables we need to explore in order to choose the rules.* -

![Screenshot 2024-10-10 at 16.03.03.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_16.03.03.png)

*How do we read this?*

Ex. for row = 0

- **instances** = There’s 85 people that have bought the antecedent aka milk, frozen foods
- **antecedent support** = 10.8% of people have bought milk, frozen foods
- **consequent support** = **prior confidence** = 42.8% of people that have bought bakery goods - not taking into account the antecedents
- **confidence (posterior)** = 83.5% of people buying *milk, frozen foods AND bakery goods* at the same time from the total instances (85)
- **lift** = *posterior confidence  / prior confidence =* 83.5 / 42.8 = 1.94
- **conf. difference**  = | posterior conf. - prior conf. | = | 83.5 - 42.8 | = 40.65
- **conf. ratio** =  *1 - (min(post,prior)/max(post,prior)) = 1 - (* 42.8*/*83.5 *)*
- **rule support** = antecedent *support * prior confidence =* 10.8 * 42.8 = 0.09% of people buying *milk, frozen foods AND bakery goods* at the same time from the total rows

How do we find negative rules?

Our criterion needs to be **confidence difference.**

![Screenshot 2024-10-10 at 16.30.51.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-10_at_16.30.51.png)

If I set a min_treshold of 0.5 and the posterior conf. is 0.49 then **the prior conf. needs to be 0.99**. aka 

$$
posteriorConf. + confidenceDiff.(threshold) = 0.49 + 0.5
$$

because, *| posterior conf. - prior conf. | = 0.49 - XX = 0.5. It’s not common to have a prior conf. of 0.99 so there’ll be barely any rules.*

<aside>
💡

The interesting rules are often those that have large differences in their confidence from the baseline value of confidence for the conclusion itself. Adding an item to the antecedent is only
informative if it significantly changes the confidence of the rule; otherwise, the simpler rule suffices.

The **Lift** statistic, which is the ratio of the rule confidence to the base rate of the consequent alone, and
which appears in model output, is sensitive to large increases in confidence.

</aside>

## **Dataiku Forum Post**

I followed the flow in the PDF resulting in the following:

With the following tresholds, I've selected the rules I want to filter out:

- metric="conf.ratio"
- min_threshold=0.5
- min_confidence=0.05
- min_rulesupport=0
- min_support=0
- max_antecedent=5

From there we can check how the confidence varies per consequent,

The **Average of conf.difference** reflects how much the prediction confidence deviates from the base rate. Higher values indicate that the rule adds more predictive value compared to just using the baseline probability. Therefore,

- **Milk** has the highest average confidence difference (0.55085), which suggests that when rules predict Milk, there is a notable increase in certainty compared to its baseline purchase rate.
- **Alcohol** and **Frozen foods** also have relatively high confidence differences (0.515 and 0.5321, respectively), indicating that rules predicting these items provide substantial additional predictive value.

We can also get the most relevant antecedent and try to focus on them when playing with the outputs of the rules,

After that, for every customer, I've checked if any rule applies to its purchases and I've selected the one with the with highest confidence.  From the resulting dataset, I've shwon the confidence with which the rules apply by Gender, Age Range and Marital Status. The confidence peaks for Married Woman over 60 with 0.96 followed by widowed male of age 31 to 40 with a 0.95. So we can infer that the rules in those groups can be applied with a great certainty.


# Session 2 : Dimension Reductions

<aside>
💾

Zoom Recording
Código de acceso: 

</aside>

<aside>
🔖

Additional Documentation : 

</aside>

<aside>
📢

**Key Takeaways**

- 
</aside>

## **Definition**

The **goal here is try to find a pattern** so that we use instead a **BIG super variable (also called FACTOR)** create from the groups of variables that share information.

The idea is that the groups contain all the information for some variables. We want to reduce complexity by reducing the amount of variables.

![Screenshot 2024-10-19 at 13.14.05.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.14.05.png)

![Screenshot 2024-10-19 at 13.15.57.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.15.57.png)

**When do we do it?**

When there’s *lots of variables* or they are *highly redundant*. We also do it when we want to *simplify things*, for example create an index.

Index = tries to summarize/condense the information of several variables in one.

Some Index examples:

- IQ
- Economic Development Index

![Screenshot 2024-10-19 at 13.21.04.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.21.04.png)

We need variables that have some information or *variability.* 

$$
Variation = Variance = Information
$$

![Screenshot 2024-10-19 at 13.23.02.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.23.02.png)

Some things we need to do to calculate this information is:

- Rescale ( normalization && standardization )
- Remove Outliers - this methods are *very* sensitive to outliers

---

The 3 factors, tell us which province is the *rich* one, because we can check the average and how each province compares to it.

![Screenshot 2024-10-19 at 13.28.45.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.28.45.png)

How do we put labels on the factors?

Once we’ve created the factors, we check for the correlation between the vars and the factors. This is called, **Factor Loading.**

<aside>
💡

The **factors are coming from transformations** of the variables. They are not linear, so the the factor loading won’t be 100%, as they don’t contain all the information in the original variables.

</aside>

## **Measuring Results: What is the process?**

![Screenshot 2024-10-19 at 13.40.12.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.40.12.png)

<aside>
💡

What is the most important **validation criterion**?

To label the factors

</aside>

![Screenshot 2024-10-19 at 13.44.59.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.44.59.png)

1. **Communalities** = % of variable information explained in the solution.
2. **Eigenvalues** = % of total information that every factor holds
    1. A component explains on average X variables. For example Component 1 explains 2.76 variables.
    2. Component 3 explains less than 1 variable, aka is not dimension reduction. So we want components with eigenvalues more than 1 variable.
    3. % of variance, of information explained by the component
    4. cumulative %, information explained by the component + the previous ones. Ex component 2’s cumulative, is the % of 1 + 2
    5. We can combine Factors + Original variables as long as they are not correlated to aim for a bigger cumulative %.
        
        ![Screenshot 2024-10-19 at 13.49.04.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.49.04.png)
        
3. **Component Matrix** = Correlations between variables and factors. It’s going to help us put labels in the components
    1. How related the variable 1 is factor 1 and factor 2
    
    ![Screenshot 2024-10-19 at 13.56.14.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.56.14.png)
    
    ![Screenshot 2024-10-19 at 13.58.32.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.58.32.png)
    

1. **Scree Plot** = it’s representing the eigenvalues. When the slope is very steep, it’s the factors you need to take, in this example factor 1 and 2.
    
    ![Screenshot 2024-10-19 at 13.59.34.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_13.59.34.png)
    
2. **Component Plot** = represents the component Matrix
    
    ![Screenshot 2024-10-19 at 14.03.43.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_14.03.43.png)
    

![Screenshot 2024-10-19 at 14.04.22.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_14.04.22.png)

We can change the **interpretability of the factors**. We can move them. The idea is that each variable is related A LOT to one factor but vey little to the other ones. 

<aside>
💡

We can rotate them, and increase the correlation with a factor. We do it when we’re not able to put some labels on the factors.

</aside>

![Screenshot 2024-10-19 at 14.05.58.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_14.05.58.png)

![Screenshot 2024-10-19 at 14.08.31.png](Machine%20Learning%20II%20116faeb4000c804ca995eeaa86317dff/Screenshot_2024-10-19_at_14.08.31.png)

## **Example in Dataiku**