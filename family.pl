% Predicates
male(john).
male(james).
male(peter).
male(joseph).
male(michael).
male(david).
male(george).

female(mary).
female(susan).
female(linda).
female(emily).
female(sarah).
female(anna).

% Facts (parent/2)
parent(john, james).
parent(john, susan).
parent(james, linda).
parent(james, peter).
parent(susan, emily).
parent(peter, joseph).
parent(mary, james).
parent(mary, susan).
parent(michael, sarah).
parent(susan, sarah).
parent(joseph, anna).
parent(anna, george).
parent(anna, david).

% Rules for family relationships
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandfather(X, Y) :- father(X, Z), parent(Z, Y).
grandmother(X, Y) :- mother(X, Z), parent(Z, Y).
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X \= Y.
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
nephew(X, Y) :- male(X), parent(Z, X), (uncle(Z, Y); aunt(Z, Y)).
niece(X, Y) :- female(X), parent(Z, X), (uncle(Z, Y); aunt(Z, Y)).
cousin(X, Y) :- parent(Z, X), parent(W, Y), (brother(Z, W); sister(Z, W)).

% Family Tree
% You can visualize the family tree based on the facts and relationships defined above.

//output
?- father(john, X).
X = james.

?- grandmother(X, emily).
X = mary ;
X = susan.

?- niece(X, anna).
?- nephew(X, anna).
X = sarah ;
X = george ;
X = david.


?- cousin(X, david).
X = george.
