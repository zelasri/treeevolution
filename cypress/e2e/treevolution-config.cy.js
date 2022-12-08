beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })

    describe('Story 7 et 5', () => {
        it('Check ', () => {
        cy.visit('http://0.0.0.0:5000/config')
        cy.visit('http://0.0.0.0:5000/config')
        cy.get('#inputStartDate').type('2022-12-13')
        cy.get('#inputEndDate').type('2023-12-20')
        cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
        cy.get('input[type=range]').as('range').invoke('val',5)
        cy.get('@range').should('have.value', 5)
       /*
        cy.visit('http://0.0.0.0:5000/simulation')
        cy.get("#configurationPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)").should('have.text', 5)
        let word1;
        cy.get('@range').should(($num) => {
            word1 = $num.text();
        });
        cy.get('#configurationPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)').should(($num) => {
            const word2 = $num.text();
            expect(word1).equal(word2);
        });
       */
        cy.get('@range')
        .invoke('val')
        .then((val1) => {
        cy.get('button[type="submit"]').click()
        cy.visit('http://0.0.0.0:5000/simulation')
        cy.get('#initSimulationBtn').click()
        cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
          .invoke('text')
          .should((text2) => {
            expect(val1).eq(text2)
          })
        })
        cy.visit('http://0.0.0.0:5000/config')
        cy.wait(500)
    
        cy.get('#inputStartDate')
        .invoke('val')
        .then((val1) => {
        // do more work here
        cy.get('button[type="submit"]').click()
        // click the button which changes the input's value
        cy.visit('http://0.0.0.0:5000/simulation')
        cy.get('#initSimulationBtn').click()
    
        cy.get('#legendTitle > div > div.col-md-9')
          .invoke('text')
          .should((text2) => {
            var text2 = text2.split(" ");
            expect(val1).eq(text2[1])
          })
        })
    
        cy.get('#legendPanel > table > tbody > tr:nth-child(3) > td:nth-child(2)').should('have.text', 0)
    
        cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(3)').should('have.text', '0 (humus)')
            })
            })
    