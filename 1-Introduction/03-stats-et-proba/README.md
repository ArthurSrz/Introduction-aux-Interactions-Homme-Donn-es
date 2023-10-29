# Pourquoi les statistiques sont-elles au coeur de la science des données ? 

Pourquoi tout de suite aborder des concepts comme les distribution, la médiane, la variance, et la statistiques quand on parle de données ? 

## La statistique comme science du très grand (et je ne parle pas de Dieu)

Car la statistique, c'est la science du **très grand et des phénomènes à grande échelle**. Les individus ou, plus généralement les faits isolés sont comme des fils que l'on peut tirer vers des données. Quand on rassemble ces fils et qu'on les classe, on obtient des paquets, qui, presque par magie ont toujours la même forme. 

Dites-vous qu'à une petite échelle, une donnée, c'est un point. Vous, moi, votre chien, c'est un point. A grande échelle, les hommes, les chiens, quand on veut regarder de quoi ils sont constitués, lorsqu'on veut les décrire rigoureusement, on a à faire à des distributions. On peut aussi penser les distributions comme le tableau d'un peintre qui donnerait dans le pointillisme. L'ensemble des petits points finissent par esquisser une image, une distribution. 

![](https://i.ytimg.com/vi/MRVbnFzvIfA/hqdefault.jpg)


## Le lien entre les données et les statistiques

Le lien entre données et statistiques se trouvent là. **LA** statistique nous donne les lois qui régissent le grand aléatoire que sont les données, qui vous caractérisent, caractérisent votre chien, me caractériste. Laissez tomber des billes aléatoirement, elles formeront toujours une forme plus ou moins semblable. Magique vous dites ? Non, juste statistique


<img src="https://j.gifs.com/vnpDlj.gif" alt="Galton Box" width="500" height="350">

Figure 1: Boite de galton qui représente une distribution normale, disponible dans la collection de Matemateca IME-USP






























### Les statistiques comme science du comportement des données.

La statistique régit le grand aléatoire que sont les données. En cela la statistique nous donne des informations sur le comportement de toute variable prise indépendamment de toutes les autres (on parle de variable _aléatoire_) : prix d'un actif financier, taille d'un individu, nombre de personnes dans un foyer, probabilité de gagner à un jeu de hasard, etc.

Une manière utile de penser la statistique peut être de la voir comme une science du comportement. A la différence près qu'elle n'étudie pas le comportement d'un être humain ou d'une espèce vivante mais plutôt le comportement des données en grandes quantités. Or, comme les êtres vivants, les nombres suivent des lois qui se retrouvent partout. 

Une loi fondamentale veut que si vous prenez une mesure et que vous répetez l'opération un très grand nombre de fois, alors l'ensemble des mesures prises (dite distribution) suivra une loi normale. Autrement dit : 
* si vous mesurez et visualisez la taille de 1000 personnes, vous obtiendrez une distribution normale
* si vous mesurez et visualisez la vitesse de pointe de 1000 chiens, vous obtiendrez une distribution normale
* si vous mesurez le poids de 1000 arbres, vous obtiendrez une distribution normale. 

Cette distribution normale prend la forme d'une cloche (d'où le fait qu'on l'a nomme aussi _distribution en cloche_) : 

![Normal Distribution with mean=0 and std.dev=1](images/normal-histogram.png)

*Distribution normale d'une variable (augmentation du salaire annuel en %) avec une moyenne de 0 et une déviation standard de 1*


> **_Studio d'interaction_**   
> 1. Sur n'importe quelle plateforme open data, téléchargez un fichier de données
> 2. Choisissez une variable quantitative
> 3. Dessinez un graphique avec en abscisse les valeurs uniques de la variable et en ordonnée le nombre de fois que chaque valeur apparait dans le jeu de données.
> 4. Regardez la forme de votre graphique 
>
>      <img src="https://media.giphy.com/media/oYtVHSxngR3lC/giphy.gif" width="200">
>


## Evaluer le comportement des données grâce à des tests d'hypothèses

L'avantage d'avoir des données avec un comportement fixe et fixés dans les lois statistiques, c'est qu'on peut établir avec une précision très précise des faits qui autrement reste dans le vague. Par exemple : votre intuition vous dit que les prix de l'immobilier autour de vous sont plus chers que dans le voisinnage de vos parents. Mais est-ce vraiment le cas ? Les données avec l'aide des statistiques peuvent permettre d'apporter une réponse claire et définitive à cette question. 

A ce stade, les statistiques vont servir de loupe pour mieux comprendre le comportement de certaines données. A la manière d'un détective. D'ailleurs, ce n'est pas un hasard si le Sherlock Holmes originel de Sir Arthur Conan Doyle fait usage d'observation et de raisonnement. statistiques dans ces enquêtes : elles sont bien un outil d'investigation. 

La différence entre Sherlock Holmes et nous tient à ce que nous ne résolvons pas des affaires criminelles mais que nous voulons **tester des hypothèses**

> **_Studio d'interaction_**  
> Mettons que nous voulons évaluer si deux variables sont fondamentalement différentes : le prix de l'immobilier autour de moi est-il différent de celui autour de chez mes parents ? 
> 1. Pour commencer, récupérez au hasard le prix de 20 actifs immobiliers autour de chez vous et 20 actifs immobiliers autour de chez vos parents.
> 3. Créez un graphique vide avec avec en abscisse des intervalles de prix de la variable et en ordonnée le nombre de fois que chaque valeur apparait dans cet intervalle
> 4. D'une couleur, dessinez la distribution des prix autour de chez vous et de l'autre, d'une autre, dessinez la distribution des prix autour de chez vos parents.
> 5. A vue d'oeil, est-ce que les prix sont différents ?
>
>      <img src="https://media.giphy.com/media/h0DX3CtxiSHw4/giphy.gif" width="200">
>    

Un test d'hypothèse, à la traduire dans un langage plus courant : 
1. vient d'un questionnement (ci-dessus : "les prix sont-ils différents ?")
2. traduit sous la forme d'une proposition hypothétique : "les prix ne sont pas différents" ou "les prix sont différents"
3. confrontée à un test statistique sur des données et aboutissant une réponse définitive : "vrai" ou "faux"
4. la réponse binaire permettant ensuite de répondre à la proposition hypothétique : oui, "les prix sont différents" ou non, "les prix ne sont pas différents" 

La clé ici est de comprendre que **le test d'hypothèse n'est qu'une manière de formuler différemment une question**. L'interactions homme-données peut à mains égards se comparer à un travail de traduction entre deux langues avec d'un côté le langage courant que nous utilisons au quotidien (facile à utiliser mais peu précis) et de l'autre le langage des données (précis mais difficile à utiliser).

Aussi s'agit-il de comprendre que la force du test statistique est de pouvoir répondre à des questions avec une très grande précision mais aussi de pouvoir dire dans quelle mesure on peut généraliser la réponse à la question. Dans notre exemple, le test va permettre de dire dans quelle mesure **tous les prix** de l'immobilier autour de chez moi sont différents de **tous les prix** autour de chez mes parents et ceux, uniquement avec des données restreintes. 

On dit alors des statistiques qu'elles ont des **capacités inférentielles** : elles permettent d'induire les caractéristiques d'un groupe général à partir de celles d'un groupe particulier. Imaginez la puissance d'une telle capacité : 
* ce sont elles qui permettent de mettre des vaccins ou des médicaments sur le marché
* de s'assurer de la rentabilité ou de l'efficacité d'un produit avant son lancement
* de prédire le comportement d'une population à partir de l'obersation du comportement d'un groupe d'individus

Le prix d'une telle puissance passe par une formalisation rigoureuse et de l'introduction de probabilités. C'est ce que nous allons voir dans la suite de cette leçon.

## Formaliser le test d'hypothèse pour apporter une réponse précise

Plus formellement, le problème que nous essayons de résoudre consiste à savoir  si **les deux distributions sont les mêmes**. Pour cela nous devons faire un test d'hypothèses. Si nous savons que les distributions sont normales, nous pouvons par exemple appliquer : 
* le **[test t de Student](https://fr.wikipedia.org/wiki/Test_t_de_Student)**
* le khi-deux de **[Pearson](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2)**

> **Anecdote**
> Le test t de Student a été nommé ainsi car son inventeur William Sealy Gosser a publié un article sous le nom de plume de "Student". Il travaillait dans une brasserie et son employeur ne voulait pas que le public sache qu'ils utilisaient des tests statistiques pour déterminer la qualité des matières premières.

### Etape 1 : déterminer la population à partir de l'échantillon grâce aux intervalles de confiance

Les statistiques confèrent une force rhétorique dans une prise de décision car elle permet de parler au nom de grands ensembles ou de généralités. Ce qui est difficile à assimilier je trouve, le saut conceptuel le plus difficile à faire pour nous (qui ne sommes pas nés statisticiens ou data scientist) est de comprendre que les grands ensembles ou les généralités sont **hautement probabilistes**. 

Pourquoi, me direz-vous:
* pourquoi ne pouvons-nous parler de grands ensembles qu'avec des probabilités ? 
* pouquoi ne pouvons-nous pas être certain, par exemple, que tous les hommes sont plus grands que les femmes ? 

Tout simplement car personne ne pourra jamais mesurer TOUS les hommes et TOUTES les femmes. De fait, nous ne pourrons jamais être certain à 100% de cette différence.

Les statistiques nous permettent de nous rapprocher de ces certitudes sans jamais les atteindre, et ce, grâce aux probabilités. 


When we talk about weights of baseball players, we assume that there is certain **random variable W** that corresponds to ideal probability distribution of weights of all baseball players (so-called **population**). Our sequence of weights corresponds to a subset of all baseball players that we call **sample**. An interesting question is, can we know the parameters of distribution of W, i.e. mean and variance of the population?

The easiest answer would be to calculate mean and variance of our sample. However, it could happen that our random sample does not accurately represent complete population. Thus it makes sense to talk about **confidence interval**.

> **Confidence interval** is the estimation of true mean of the population given our sample, which is accurate is a certain probability (or **level of confidence**).


Suppose we have a sample X<sub>1</sub>, ..., X<sub>n</sub> from our distribution. Each time we draw a sample from our distribution, we would end up with different mean value &mu;. Thus &mu; can be considered to be a random variable. A **confidence interval** with confidence p is a pair of values (L<sub>p</sub>,R<sub>p</sub>), such that **P**(L<sub>p</sub>&leq;&mu;&leq;R<sub>p</sub>) = p, i.e. a probability of measured mean value falling within the interval equals to p.


### Etape 2 : calculer des intervalles de confiance pour une variable

> It does beyond our short intro to discuss in detail how those confidence intervals are calculated. Some more details can be found [on Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval). In short, we define the distribution of computed sample mean relative to the true mean of the population, which is called **student distribution**.

If we want to estimate the mean &mu; of our population with confidence p, we need to take *(1-p)/2-th percentile* of a Student distribution A, which can either be taken from tables, or computer using some built-in functions of statistical software (eg. Python, R, etc.). Then the interval for &mu; would be given by X&pm;A*D/&radic;n, where X is the obtained mean of the sample, D is the standard deviation.

> **Note**: We also omit the discussion of an important concept of [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), which is important in relation to Student distribution. You can refer to more complete books on statistics to understand this concept deeper.

An example of calculating confidence interval for weights and heights is given in the [accompanying notebooks](notebook.ipynb).

| p | Weight mean |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Notice that the higher is the confidence probability, the wider is the confidence interval. 


### Etape 3 : comporer les intervalles de confiance de chaque variable


#### Analyse visuelle

However, it is not always obvious whether we can make this conclusion. From the discussion above we know that each mean has an associated confidence interval, and thus this difference can just be a statistical error. We need some more formal way to test our hypothesis.

Let's compute confidence intervals separately for heights of first and second basemen:

| Confidence | First Basemen | Second Basemen |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

We can see that under no confidence the intervals overlap. That proves our hypothesis that first basemen are higher than second basemen.

#### Analyse numérique 

In Student t-test, we compute so-called **t-value**, which indicates the difference between means, taking into account the variance. It is demonstrated that t-value follows **student distribution**, which allows us to get the threshold value for a given confidence level **p** (this can be computed, or looked up in the numerical tables). We then compare t-value to this threshold to approve or reject the hypothesis.

In Python, we can use the **SciPy** package, which includes `ttest_ind` function (in addition to many other useful statistical functions!). It computes the t-value for us, and also does the reverse lookup of confidence p-value, so that we can just look at the confidence to draw the conclusion.

For example, our comparison between heights of first and second basemen give us the following results: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
In our case, p-value is very low, meaning that there is strong evidence supporting that first basemen are taller.

There are also different other types of hypothesis that we might want to test, for example:
* To prove that a given sample follows some distribution. In our case we have assumed that heights are normally distributed, but that needs formal statistical verification. 
* To prove that a mean value of a sample corresponds to some predefined value
* To compare means of a number of samples (eg. what is the difference in happiness levels among different age groups)



## Law of Large Numbers and Central Limit Theorem

One of the reasons why normal distribution is so important is so-called **central limit theorem**. Suppose we have a large sample of independent N values X<sub>1</sub>, ..., X<sub>N</sub>, sampled from any distribution with mean &mu; and variance &sigma;<sup>2</sup>. Then, for sufficiently large N (in other words, when N&rarr;&infin;), the mean &Sigma;<sub>i</sub>X<sub>i</sub> would be normally distributed, with mean &mu; and variance &sigma;<sup>2</sup>/N.

> Another way to interpret the central limit theorem is to say that regardless of distribution, when you compute the mean of a sum of any random variable values you end up with normal distribution. 

From the central limit theorem it also follows that, when N&rarr;&infin;, the probability of the sample mean to be equal to &mu; becomes 1. This is known as **the law of large numbers**.

## Covariance and Correlation

One of the things Data Science does is finding relations between data. We say that two sequences **correlate** when they exhibit the similar behavior at the same time, i.e. they either rise/fall simultaneously, or one sequence rises when another one falls and vice versa. In other words, there seems to be some relation between two sequences.

> Correlation does not necessarily indicate causal relationship between two sequences; sometimes both variables can depend on some external cause, or it can be purely by chance the two sequences correlate. However, strong mathematical correlation is a good indication that two variables are somehow connected.

 Mathematically, the main concept that shows the relation between two random variables is **covariance**, that is computed like this: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. We compute the deviation of both variables from their mean values, and then product of those deviations. If both variables deviate together, the product would always be a positive value, that would add up to positive covariance. If both variables deviate out-of-sync (i.e. one falls below average when another one rises above average), we will always get negative numbers, that will add up to negative covariance. If the deviations are not dependent, they will add up to roughly zero.

The absolute value of covariance does not tell us much on how large the correlation is, because it depends on the magnitude of actual values. To normalize it, we can divide covariance by standard deviation of both variables, to get **correlation**. The good thing is that correlation is always in the range of [-1,1], where 1 indicates strong positive correlation between values, -1 - strong negative correlation, and 0 - no correlation at all (variables are independent). 

**Example**: We can compute correlation between weights and heights of baseball players from the dataset mentioned above:
```python
print(np.corrcoef(weights,heights))
```
As a result, we get **correlation matrix** like this one:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Correlation matrix C can be computed for any number of input sequences S<sub>1</sub>, ..., S<sub>n</sub>. The value of C<sub>ij</sub> is the correlation between S<sub>i</sub> and S<sub>j</sub>, and diagonal elements are always 1 (which is also self-correlation of S<sub>i</sub>).

In our case, the value 0.53 indicates that there is some correlation between weight and height of a person. We can also make the scatter plot of one value against the other to see the relationship visually:

![Relationship between weight and height](images/weight-height-relationship.png)

> More examples of correlation and covariance can be found in [accompanying notebook](notebook.ipynb).

## Conclusion

In this section, we have learnt:

* basic statistical properties of data, such as mean, variance, mode and quartiles
* different distributions of random variables, including normal distribution
* how to find correlation between different properties
* how to use sound apparatus of math and statistics in order to prove some hypotheses, 
* how to compute confidence intervals for random variable given data sample

While this is definitely not exhaustive list of topics that exist within probability and statistics, it should be enough to give you a good start into this course.



## Credits

Cette leçon a été crée avec ♥️ by [Dmitry Soshnikov](http://soshnikov.com) et éditée par [Arthur Sarazin]()
