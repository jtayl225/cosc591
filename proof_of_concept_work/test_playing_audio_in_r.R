library(shiny)
library(shinydashboard)
library(readr)
library(tuneR)
library(seewave)

# Define UI for application that draws a histogram
#Soundfile <- readWave("F:/UNE/COSC591/beep.wav") need to upload as I cant load local resources, so have to find a .wav online
#class(Soundfile)
ui <- dashboardPage(
  dashboardHeader(title = "Example Audio Play"),
  
  dashboardSidebar(
    sidebarMenu(
      menuItem("Play Audio", tabName = "playaudio", icon = icon("dashboard"))
    )),
  
  dashboardBody(
    tabItems(
      tabItem(tabName = "playaudio",
              fluidRow(
                box(title = "Controls", width = 4,
                    actionButton("playsound", label = "Play The Rebuilt Sound!"))
              )
      )
    )
  )
)


# Define server logic required to draw a histogram
server <- function(input, output) {
  #Soundwav <- Soundfile
  #savewav(Soundwav, filename = "www\\Soundwavexported.wav")
  
  
  observeEvent(input$playsound, {
    insertUI(selector = "#playsound",
             where = "afterEnd",
             ui = tags$audio(src = "https://wavlist.com/wav/bj.wav", type = "audio/wav", autoplay = NA, controls = NA, style="display:none;")
    )
  })
  
}


# Run the application 
shinyApp(ui = ui, server = server)