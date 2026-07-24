// EN: Checks if the API responded successfully (HTTP 200)
// Verifica se a API respondeu com sucesso (HTTP 200)
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// EN: Ensures the response body contains the ID of the created/requested record
// Garante que o corpo da resposta traz o ID do registro criado/solicitado
pm.test("Response contains task ID", function () {
    const response = pm.response.json();
    pm.expect(response).to.have.property("id");
});
