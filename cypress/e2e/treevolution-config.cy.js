beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })
    
describe('Story 1', () => {
    it('Check home page', () => {
    cy.visit('http://0.0.0.0:5000')
    cy.wait(500) // add some delay
    cy.get('h2').contains('Welcome to the Treevolution simulator') // first test
    })
    })