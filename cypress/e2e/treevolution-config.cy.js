beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 13', () => {
        it('Check the value day in config page', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.get('#inputStartDate').type('2022-12-13')
        cy.get('#inputEndDate').type('2023-12-20')
        cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
        cy.get('input[type=range]').as('range').invoke('val',5)
        cy.get('@range').should('have.value', 5)
        cy.get('button[type="submit"]').click()
        
        
        cy.visit('http://0.0.0.0:5000/simulation')
                cy.get('#initSimulationBtn').click()
                cy.get('#runSimulationBtn').click()
               
                cy.get('#simulationProgress',{timeout: 20000}).should('contain', '100%')
//verification que le nombre des arbres et le meme apres la pause               
                cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .then((text1) => {
                cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .should((text2) => {
                expect(text1).eq(text2)
            })
            })
            cy.visit('http://0.0.0.0:5000/config')
            cy.get('#inputEndDate')
            .invoke('val')
            .then((val1) => {
            // do more work here
            // click the button which changes the input's value
            cy.visit('http://0.0.0.0:5000/simulation')
            cy.get('#legendTitle > div > div.col-md-9')
              .invoke('text')
              .should((text2) => {
                var text2 = text2.split(" ");
                expect(val1).eq(text2[1])
              })
            })


                        })
                        })
