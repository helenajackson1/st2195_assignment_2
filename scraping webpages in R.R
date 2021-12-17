library(rvest)

# read HTML
url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

# see Table
table = url %>%
  read_html() %>%
  html_nodes(".wikitable")%>%
  html_table()

# data frame
as.data.frame(table)

# export to csv
write.csv(table, "C:/Users/norrs/OneDrive/Documents/UNIVERSITY/R/R_csv.csv")
