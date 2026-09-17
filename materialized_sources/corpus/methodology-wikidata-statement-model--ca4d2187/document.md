# Wikidata : Data model

Bahasa Indonesia

Deutsch

English

Nederlands

dansk

español

français

polski

русский

українська

日本語

Wikidata represents entities as data items (e.g. Tim Berners-Lee (Q80) and CERN (Q42944) are data items).
Knowledge about data items is represented via statements , whose basic structure consists of a subject , a predicate and an object .

For example: Tim Berners-Lee (Q80) employer (P108) CERN (Q42944)

The subject of a statement  is usually a data item — in this case, Tim Berners-Lee (Q80) .

The predicate of a statement is always a property — in this case, employer (P108) .

The object of a statement is a value of the data type of the property — in this case, an item, CERN (Q42944) .

The property used in a statement determines both the meaning of the statement (i.e. the nature of the relationship between the subject and the object), as well as which values may be used, as specified by its data type .

For example, in the example above we used the property employer (P108) , whose values must have the data type Item ,
allowing a data item to be set as the object of the statement (in the case of our example, CERN (Q42944) ).

An example of a property with a different data type is start time (P580) , whose values must be of data type Point in time , so it can only be used to state a point in time.

Wikidata also allows statements to be qualified with further properties, which are called qualifiers . For example, we might state Tim Berners-Lee (Q
