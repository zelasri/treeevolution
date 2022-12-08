beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 5', () => {
        it('Check ', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500) // add some delay
        cy.get('#inputStartDate').type('2022-12-13').should('have.value','2022-12-13')
        cy.get('#inputEndDate').type('2023-12-20').should('have.value','2023-12-20')
        cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
        cy.get('input[type=range]').invoke('val',5)
        cy.get('#inputDaysNumber').invoke('val',3)
        cy.get('#inputSeed').invoke('val',42)
        cy.get('button[type="submit"]').click()
        cy.wait(500)
        cy.get('div[role="alert"] > div').contains('Configuration has been updated. The simulation has been reset.')
        })
        })
    
    

