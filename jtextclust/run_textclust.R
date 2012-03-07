library(tm)

INDIR <- "../../data/"


read_data <- function(fname=paste(INDIR, "jarchiven.csv", sep='/')) {
  x <- read.csv(fname, as.is=T)
  ds <- DataframeSource(x[,'clue',drop=F])
  corp <- Corpus(ds)
  corp <- tm_map(corp, stripWhitespace)
  corp <- tm_map(corp, tolower)
  corp <- tm_map(corp, removeWords, stopwords("english"))
  corp
}

do_kmeans <- function(corp, n=40) {
  #This is a rough first effort - 
  #TODO: should come up with a document similarity measure and hClust on that. maybe dissimilarity()
  
  tdm <- TermDocumentMatrix(corp)
  km <- kmeans(tdm, n)
  print(lapply(sort(unique(km$cluster)), function(x) paste(names(km$cluster[km$cluster == x]))))
  km
}


#TODO: function to take kmeans output and assign cluster number back to original document.
main <- function() {
  corp <- read_data()
  do_kmeans(corp)
}

