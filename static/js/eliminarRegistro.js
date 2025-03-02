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