from MongoDB import *
from SurrealDB import *
from SqLite import *
from signup import *


for i in userall:
    IMDB(i[0], i[1], i[2], i[3], i[4])