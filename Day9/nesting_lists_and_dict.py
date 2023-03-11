##
dictionary1 = {
    "key1" :  [],
    "key2" : {dict}
}

capitals = {
            "France": "Paris",
            "Germany": "Berin"
}
## Example of nesting list inside the list
lists1 = ["A","B", ["C","D"],"E "]
#print(lists1)

## Nesting the list inside the Dictionary 
travel_log  = {
            "France": ["Paris","Lili","Dijion" ],
            "Germany": ["Berlin","Frankfurt", "Hamburg"]

}

## Nesting Dictionary inside Dictionary 
travel_log  = {
            "France": {"Cities_Visted": ["Paris","Lili","Dijion" ], "total_visits":12},
            "Germany": {"Cities_Visited": ["Berlin","Frankfurt","Hamburg"],"total_visits": 14}
}

print(travel_log["France"])

## Nesting Dictionary inside lists 
list2 = [
          {
                "key1": "value1",
                "key2": "value2"
         } 
 ]

# Nesting Dictionary insides List Example 

travel_log1  = [
    {
    "Country": "France",
    "Cities_Visted": ["Paris","Lili","Dijion" ], 
    "total_visits":12,
    
    "Country": "Germany",
    "Cities_Visited": ["Berlin","Frankfurt","Hamburg"],
    "total_visits": 5
    }
]

