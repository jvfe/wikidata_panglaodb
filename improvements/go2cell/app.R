#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(WikidataQueryServiceR)
library(readr)
library(rdflib)

# https://w.wiki/mYb
geneontology_df <- read_csv2("go_df.csv")

markers_ttl <- rdf_parse("human_cell_type_markers_13_11_2020.ttl")
query_markers <- 'SELECT  ?cell_type ?gene WHERE {
 ?cell_type ?p ?gene
}'

markers_df <- rdf_query(markers_ttl, query_markers)

# https://w.wiki/mYZ
cell_type_df <- read_csv("cell_type_df.csv")

library(dplyr)

df <- full_join(markers_df, cell_type_df)
df2 <- inner_join(geneontology_df, df)

processes = unique(df2[,"processLabel"])

ui <- fluidPage(

    # Application title
    titlePanel("v0 GO to Cell Type"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            selectizeInput("goterm",
                        "GO Term",
                        selected = "muscle contraction",
                        choices = processes)
        ),

        # Show a plot of the generated distribution
        mainPanel(
            tableOutput('df_lean')
    
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    df_lean <- eventReactive({
        input$goterm
    }, {
        df_lean <-
            df2 %>% filter(
                processLabel ==  input$goterm,
            ) %>% select(cell_typeLabel, processLabel, goterm, geneLabel)
        return(df_lean)
    })
    output$df_lean <- renderTable({ df_lean() })
}
# Run the application 
shinyApp(ui = ui, server = server)
