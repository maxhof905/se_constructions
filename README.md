## 1 Introduction

### SE

The present thesis explores how the clitic SE and its unique linguistic characteristics are handled in NLP tasks in Spanish and Portuguese. The clitic SE is a widely used element in Spanish and Portuguese that occurs in various linguistic contexts. Depending on the context SE can take on different syntactic roles and impacts the semantic reading of the sentence. The somber but interesting Spanish verbal form se mató ‘se kill.PST.3SG’, illustrates this behavior (Otero, 2002, p. 166):

a. Durante la Guerra se mató más de lo que se cree. ‘during the war more people were killed than is commonly believed’

b. El turista que se mató tras saltar de un acantilado[...] ‘the tourist who died after jumping off a cliff’

c. Alguien se mató. ‘somebody commited suicide’

d. Maria se mató por conseguir esta oportunidad. ‘Maria worked really hard to get this opportunity'.


The semantic implications of SE and its syntactic behavior have been examined in numerous studies from a variety of perspectives, not only for Spanish or 
Portuguese, but also regarding other Romance languages. The perspective that this thesis takes is that of how the knowledge from the linguistic literature on 
SE can be incorporated into NLP tasks in a manner that contributes to improving the performance of such tasks. Three main research questions arose from 
taking this point of view onto the intersection of Romance linguistics and computational linguistics:

(1) how accurately are the separate grammatical functions of SE identified when it comes to the natural language processing tasks of dependency parsing and part-of-speech tagging?

(2) is the identification of the grammatical functions that SE can fulfil equally accurate in Spanish and Portuguese?

(3) does the Universal Dependencies tag set allow for an accurate dependency labeling of all the grammatical functions that Spanish and Portuguese SE can fulfil?

### Active Learning and Transformer Models
These research interests will be approached through examining the existing literature on SE in NLP and through performing a machine learning experiment. The 
goal of the machine learning experiment is to explore whether the learning strategy called ***active learning*** proves useful in computationally processing 
and classifying occurrences of SE in Spanish and Portuguese. The particularity of active learning as a machine learning strategy is that it makes it possible 
to train well-performing machine learning models for linguistic classification tasks with limited amounts of labeled data (see Olsson, 2009; Settles, 2009). 

A secondary part of the active learning experiment consists in training Spanish and Portuguese transformer models on classifying occurrences of SE. The 
performance of these transformer models is used to contrast the performance that the active-learning-based models achieve. The general design of active 
learning tasks and the availability of labeled linguistic data as well as the architecture of the trained machine learning models and the transformer models 
will be thoroughly discussed.

The motivation for exploring how Spanish and Portuguese SE are handles in natural language and processing stems from the observations that a) the linguistic 
analysis of SE is highly complex and that b) the proper identification of the syntactic function SE fulfils in a sentence is decisive for a range of natural 
language processing that are concerned with semantics, such as semantic role assignment, question answering or sentiment analysis. The motivation for 
exploring if and to which extent active-learning-based models are suited to classify Spanish and Portuguese occurrences of SE is not so much the observation 
but rather the experience that labeled linguistic data that could be used to satisfactorily train a classification model that is not based on active learning 
is scarce.
