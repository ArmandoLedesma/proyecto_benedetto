function deleteEntity(id, uri, renderTable, entityName = 'registro') {
    fetch(`${uri}/${id}`, {
        method: 'DELETE'
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al eliminar el ${entityName}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(`${entityName} eliminado:`, data);
            renderTable();
        })
        .catch(error => {
            console.error(`Error al eliminar el ${entityName}:`, error);
        });
}


// Ejemplo de uso:
// deleteEntity(1, 'http://localhost:8080/api/registros', renderTable);
// llamar esta funcion desde donde es incluida
// en el archivo html
// <script src="static/js/eliminarRegistro.js"></script>
//como usar la funcion
// deleteEntity(1, 'http://localhost:8080/api/registros', renderTable);
// deleteEntity(1, 'http://localhost:8080/api/registros', renderTable, 'usuario');
// deleteEntity(1, 'http://localhost:8080/api/registros', renderTable, 'producto');
// deleteEntity(1, 'http://localhost:8080/api/registros', renderTable, 'categoria');