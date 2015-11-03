def read_text():
    quotes = open(r"C:\Users\rajawatk\Desktop\movie_quotes.txt")  
    contents_of_file = quotes.read()   
    print(contents_of_file)    
    quotes.close()    
read_text()
