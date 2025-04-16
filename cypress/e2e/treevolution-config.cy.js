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
    it(' Vérifier que les champs nombres de jours et nombres d arbres indiquent correctement', () => {
    cy.visit('http://0.0.0.0:5000/config')
    cy.wait(500) // add some delay
    cy.get('input[type=range]').as('range').invoke('val',5)
    cy.get('@range').should('have.value', 5)

    })
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

describe('Story 4', () => {
    it(' date de fin de simulation inférieure à celle de début. Un message d’erreur peut-être vérifié', () => {
    cy.visit('http://0.0.0.0:5000/config')
    cy.wait(500) // add some delay
    cy.get('#inputKindsTree').select('treevolution.models.trees.oak.Ash')
    cy.get('button[type="submit"]').click() // apres click cy.wait
    cy.wait(500) 
        })
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

    




    describe('Story 8', () => {
        it(' le nombre d’espèces d’arbres séléctionnés est correct', () => {
            cy.visit('http://0.0.0.0:5000/config')
            cy.get('input[type=range]')
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
            cy.wait(500)
            })
            })


    describe('Story 9', () => {
                it('Lorsqu’une simulation est créée depuis l’onglet /simulation à partir d’une configuration. Celle-ci peut-être supprimée si la configuration vient à changer.', () => {
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

    describe('Story 10', () => {
        //  verification que le nombre des arbres evolue a la fin de la simulation

        it('verification que le nombre des arbres evolue a la fin de la simulation', () => {
            cy.visit('http://0.0.0.0:5000/simulation')
            cy.get('#initSimulationBtn').click()
            cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
            .invoke('text')
            .then((text1) => {
            cy.get('#runSimulationBtn').click()
            cy.get('#simulationProgress',{timeout: 20000}).should('contain', '100%')
            cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
            .invoke('text')
            .should((text2) => {
                expect(text1).not.eq(text2)
            })
            })
            })
            })

    describe('Story 11', () => {
            it('Lorsqu’une simulation est exécutée, puis mise en pause,la date et le nombre d’arbres sont restés fixes après un certain délai.', () => {
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



    describe('Story 12', () => {
            it('Lorsqu’une simulation est exécutée, puis mise en pause,il est possible de la réinitialiser.', () => {
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


         describe('Story 13', () => {
                it('Check the value day in config page', () => {
                cy.visit('http://0.0.0.0:5000/simulation')
                cy.get('#initSimulationBtn').click()
                cy.get('#runSimulationBtn').click()
               
                cy.get('#simulationProgress',{timeout: 20000}).should('contain', '100%')
//verification que le nombre des arbres et le meme apres la pause               
                cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .then((text1) => {
                cy.get('#legendPanel > table > tbody > tr:nth-child(2) > td:nth-child(2)')
                .invoke('text')
                .should((text2) => {
                expect(text1).eq(text2)
            })
            })
            cy.visit('http://0.0.0.0:5000/config')
            cy.get('#inputEndDate')
            .invoke('val')
            .then((val1) => {
            // do more work here
            // click the button which changes the input's value
            cy.visit('http://0.0.0.0:5000/simulation')
            cy.get('#legendTitle > div > div.col-md-9')
              .invoke('text')
              .should((text2) => {
                var text2 = text2.split(" ");
                expect(val1).eq(text2[1])
              })
            })


                        })
                        })