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
describe('Story 2', () => {
    it('Check the value day in config page', () => {
    cy.visit('http://0.0.0.0:5000/config')
    cy.wait(500) // add some delay
    cy.get('input[type=range]').as('range').invoke('val',5)
    cy.get('@range').should('have.value', 5)

    })
    })

    describe('Story 4', () => {
        it('Check the value day in config page', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500) // add some delay
        cy.get('select').eq(0).select('treevolution.models.trees.oak.Ash')
        .should('have.value','Ash (treevolution.models.trees.oak.Ash)')

      // confirm the selected value
       
    
        })
        })
    describe('Story 5', () => {
        it('Check the value day in config page', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500) // add some delay
        cy.get('#inputKindsTree').should('not.be.empty')

            })
            })