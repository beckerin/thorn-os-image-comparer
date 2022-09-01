# thorn-os-image-comparer

# Params
 - ph: type int range (0 - 1) which correspond from 0 to 100% percent of similiarity
   - ex : ph=0.75
 - id1: type string[]
   - ex : id1=https://google.com/favicon.jpg&id1=https://facebook.com/favicon.jpg
 - id2: type string[]
   - ex : id2=https://facebook.com/favicon.jpg
  
  
  # Returns
   - string[]
   ex: 
   [
    "https://facebook.com/favicon.jpg",
    "https://facebook.com/favicon.jpg"
   ]
   
# Example
    http://127.0.0.1:3000/image?ph=0.564&id1=https://google.com/favicon.jpg&id1=https://facebook.com/favicon.jpg&id2=https://facebook.com/favicon.jpg
returns : [
"https://facebook.com/favicon.jpg",
"https://facebook.com/favicon.jpg"
]
