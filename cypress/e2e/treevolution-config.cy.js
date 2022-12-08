beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 2', () => {
    it(' Vérifier que les champs nombres de jours et nombres d arbres indiquent correctement', () => {
    cy.visit('http://0.0.0.0:5000/config')
    cy.wait(500) // add some delay
    cy.get('input[type=range]').as('range').invoke('val',5)
    cy.get('@range').should('have.value', 5)

    })
    })

