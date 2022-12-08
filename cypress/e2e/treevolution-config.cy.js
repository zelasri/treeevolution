beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 4', () => {
        it('  possible de valider une configuration n’ayant aucun type d’arbre sélectionné', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500) // add some delay
        cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
        cy.get('button[type="submit"]').click() // apres click cy.wait
        cy.wait(500) 
            })
            })
    
    

