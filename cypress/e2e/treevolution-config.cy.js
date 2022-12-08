beforeEach(() => {
    cy.restoreLocalStorage() // entre chaque it restaure le local storage
    cy.wait(500)
    cy.visit('http://0.0.0.0:5000') // requiert également un rafraichissement de page
    })

afterEach(() => {
    cy.saveLocalStorage() // sauvegarde le local storage après chaque it
    })


describe('Story 11', () => {
        it('Lorsqu’une simulation est exécutée, puis mise en pause,la date et le nombre d’arbres sont restés fixes après un certain délai.', () => {
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
        cy.wait(200)
//  verification que le nombre des arbres et le meme apres la pause

        cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
        .invoke('text')
        .then((text1) => {
        cy.get('#runSimulationBtn').click()
        cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
        .invoke('text')
        .should((text2) => {
            expect(text1).eq(text2)
        })
        })

        cy.get('#runSimulationBtn').click()
        cy.wait(200)
        cy.get('#runSimulationBtn').click()
//  verification que la date legend et le meme apres la pause
        cy.get('#legendTitle > div > div.col-md-9')
        .invoke('text')
        .then((text1) => {
               var text1 = text1.split(" ");
        cy.get('#legendTitle > div > div.col-md-9')
        .invoke('text')
        .should((text2) => {
            var text2 = text2.split(" ");
            expect(text1[1]).eq(text2[1])
                })
                })

//  verification que le nombre des seeds et le meme apres la pause               

        cy.get('#legendPanel > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        .invoke('text')
        .then((text1) => {
        cy.get('#legendPanel > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        .invoke('text')
        .should((text2) => {
        expect(text1).eq(text2)
                 })
                })
           
        })
       
        
        
        
})
