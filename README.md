# QuizML
A simple markup language to create quiz data by using a concise and easy to remember grammar.
The goal of this project is to facilitate quiz generation and to provide data portability. 
It is possible to version control the plain quiz data and generate a nwe quiz data source on-demand.

```
Multi-choice capitals quiz 
@quiz Capitals 
@desc Select the correct capital 
@tags easy, multi choice 
? The capital of Sweden is @blank.
+ Stockholm
- Helsinki
- Oslo
- Copenhagen
```

```
Drag and drop
@quiz Capital match quiz
@desc Can you pick the correct capital for each country? 
@tags countries, cities, geography 
? Sweden 
+ Stockholm

? Ireland
+ Dublin
```

```
True/False
@quiz Capitals
@desc Select either true or false 
@tags countries, cities, geography 
+ Stockholm is the capital of Sweden 
- The capital of Scotland is Dublin
```
