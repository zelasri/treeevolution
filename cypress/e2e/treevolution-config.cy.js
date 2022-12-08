beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 12', () => {
        it('Lorsqu’une simulation est exécutée, puis mise en pause,il est possible de la réinitialiser.', () => {
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
                cy.get('#runSimulationBtn').click()
                cy.get('#initSimulationBtn').click()

                cy.get('#simulationProgress').should('have.text', '0%')
//  les informations de simulation réinitialisées  à la configuration courant,
//idee c'est comparer info de la configuration et les info de la simulation
                cy.get('#configurationPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .then((text1) => {
                cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .should((text2) => {
                    expect(text1).eq(text2)
                })
                })
                
                cy.get('#configurationPanel > table > tbody > tr:nth-child(3) > td:nth-child(2)')
                .invoke('text')
                .then((text1) => {
                cy.get('#legendTitle > div > div.col-md-9')
                .invoke('text')
                .should((text2) => {
                    var text2 = text2.split(" ");
                    expect(text1).eq(text2[1])
                })
                })
                cy.get("td").contains("Kinds").parent().siblings().first().should("contain","Ash")
                })
                    })


         