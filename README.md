# thorn-os-image-comparer

# Params
 - ph type int range ( 0 - 1)
  ex : ph=0.75 ( which correspond to 75% percent of similiarity )
 - id1 type string[]
  ex : id1=https://google.com/favicon.jpg&id1=https://facebook.com/favicon.jpg
 - id2 type string[]
  ex : id2=https://facebook.com/favicon.jpg
  
  # Returns
   - string[]
   ex: 
   [
    "https://facebook.com/favicon.jpg",
    "https://facebook.com/favicon.jpg"
   ]
