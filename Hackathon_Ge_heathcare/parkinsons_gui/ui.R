shinyUI(fluidPage(
  titlePanel(h1("Parkinson's Disease Prediction")),
  
  sidebarLayout(position = "right",
                sidebarPanel( h3("Results of the Analysis"),
                              textOutput("text1")),
  mainPanel(h3("Fill in the Data of the Patient"),
            fluidRow(
              column(3, 
                     checkboxGroupInput("checkGroup", 
                                        label = h3("Checkbox group"), 
                                        choices = list("Choice 1" = 1, 
                                                       "Choice 2" = 2, "Choice 3" = 3),
                                        selected = 1)),
              column(3, 
                     numericInput("NP1", 
                                        label = h3("NP1"),value=0 )),
              column(3,
                     h3("Buttons"),
                     actionButton("action", label = "Action"),
                     br(),
                     br(), 
                     submitButton("Submit"))
              
              )   
            ))
  ))