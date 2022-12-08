beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 3', () => {
        it(' date de fin de simulation inférieure à celle de début. Un message d’erreur peut-être vérifié', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500) // add some delay
        cy.get('#inputStartDate').type('2022-11-13').should('have.value','2022-11-13')
        cy.get('#inputEndDate').type('2022-11-04').should('have.value','2022-11-04')
        cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
        cy.get('#inputDaysNumber').invoke('val',3)
        cy.get('#inputSeed').invoke('val',42)
        cy.get('button[type="submit"]').click() // apres click cy.wait
        cy.wait(500)
        cy.get('div[role="alert"] > div').contains('Invalid start date and end date.') 
        })
        })
    

