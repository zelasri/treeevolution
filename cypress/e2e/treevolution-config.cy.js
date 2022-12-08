beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 9', () => {
        it('Lorsqu’une simulation est créée depuis l’onglet /simulation à partir d’une configuration. Celle-ci peut-être supprimée si la configuration vient à changer.', () => {
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
        cy.visit('http://0.0.0.0:5000/config')
        cy.get('#inputStartDate').type('2022-12-15')
        cy.get('button[type="submit"]').click()
        cy.wait(500)
        cy.visit('http://0.0.0.0:5000/simulation')
        cy.get('#legendPanel > div > p > i').contains('No current simulation available')
                
                })
            })