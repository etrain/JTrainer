library(tm)

INDIR <- "../data/"
OUTDIR <- INDIR


read_data <- function(fname=paste(INDIR, "jarchive.csv", sep='/')) {
  x <- read.csv(fname, as.is=T)
  print("Read data")
  ds <- DataframeSource(x[,'clue',drop=F])
  print('created data frame')
  corp <- Corpus(ds)
  print('created corpus')
  corp <- tm_map(corp, stripWhitespace)
  print('stripped whitespace')
  corp <- tm_map(corp, tolower)
  print('lowercased')
  corp <- tm_map(corp, removeWords, stopwords("english"))
  print('stripped stopwords')
  list(df=x, corp=corp)
}

do_kmeans <- function(corp, n=30) {
  #TODO: figure out how to force algo into using more evenly sized clusters.
  
  dtm <- DocumentTermMatrix(corp)
  print('created dtm')
  removeSparseTerms(dtm, 0.999)
  print('removed sparse terms')

  kmeans(dtm, n)
}

write_data <- function(df, fname=paste(OUTDIR, "jarchive-clustered.csv", sep='/')) {
  write.csv(df, fname, row.names=F)
}

#TODO: function to take kmeans output and assign cluster number back to original document.
main <- function(debug=F) {
  dat <- read_data()
  
  km <- do_kmeans(dat$corp)
  dat$df$cluster <- km$cluster

  write_data(dat$df)

  if(debug) return(list(df=dat$df, km=km))
}

main()
