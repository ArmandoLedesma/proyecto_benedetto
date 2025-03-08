// Archivo: pagination.js
// Controlador genérico de paginación para tablas de datos

/**
 * Configuración y estado de la paginación
 */
const paginationState = {
    currentPage: 1,
    totalPages: 1,
    recordsPerPage: 10,
    allRecords: [],
    fetchUrl: '',
    renderCallback: null,
    recordsKey: 'records',
    tableBodyId: 'tableBody'
};

/**
 * Inicializa el sistema de paginación
 * @param {Object} config - Configuración de la paginación
 * @param {string} config.fetchUrl - URL para obtener los datos
 * @param {Function} config.renderCallback - Función para renderizar cada fila
 * @param {string} config.recordsKey - Clave para acceder a los registros en la respuesta JSON
 * @param {string} config.tableBodyId - ID del tbody donde se renderizarán los datos
 * @param {number} config.recordsPerPage - Registros por página (opcional, por defecto 10)
 */
function initPagination(config) {
    // Actualizar la configuración
    paginationState.fetchUrl = config.fetchUrl;
    paginationState.renderCallback = config.renderCallback;
    paginationState.recordsKey = config.recordsKey || 'records';
    paginationState.tableBodyId = config.tableBodyId || 'tableBody';
    
    if (config.recordsPerPage) {
        paginationState.recordsPerPage = config.recordsPerPage;
    }
    
    // Inicializar los eventos de paginación
    initPaginationEvents();
    
    // Cargar datos
    fetchRecords();
}

/**
 * Inicializa los eventos para los controles de paginación
 */
function initPaginationEvents() {
    // Evento para botón "Anterior"
    const prevPageBtn = document.getElementById('prevPageBtn');
    if (prevPageBtn) {
        prevPageBtn.addEventListener('click', () => {
            if (paginationState.currentPage > 1) {
                paginationState.currentPage--;
                renderPage(paginationState.currentPage);
                updatePaginationControls();
            }
        });
    }

    // Evento para botón "Siguiente"
    const nextPageBtn = document.getElementById('nextPageBtn');
    if (nextPageBtn) {
        nextPageBtn.addEventListener('click', () => {
            if (paginationState.currentPage < paginationState.totalPages) {
                paginationState.currentPage++;
                renderPage(paginationState.currentPage);
                updatePaginationControls();
            }
        });
    }
    
    // Evento para selector de registros por página (si existe)
    const recordsPerPageSelect = document.getElementById('recordsPerPageSelect');
    if (recordsPerPageSelect) {
        recordsPerPageSelect.addEventListener('change', () => {
            paginationState.recordsPerPage = parseInt(recordsPerPageSelect.value);
            paginationState.currentPage = 1; // Resetear a primera página
            fetchRecords();
        });
    }
}

/**
 * Obtiene los registros desde la API
 */
function fetchRecords() {
    fetch(paginationState.fetchUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al obtener datos de ${paginationState.fetchUrl}`);
            }
            return response.json();
        })
        .then(data => {
            // Almacenar todos los registros
            paginationState.allRecords = data[paginationState.recordsKey];
            
            // Actualizar el total de registros en la UI
            const totalRecordsEl = document.getElementById('totalRecords');
            if (totalRecordsEl) {
                totalRecordsEl.textContent = paginationState.allRecords.length;
            }
            
            // Calcular el total de páginas
            paginationState.totalPages = Math.ceil(
                paginationState.allRecords.length / paginationState.recordsPerPage
            );
            
            // Asegurarse de que la página actual es válida
            if (paginationState.currentPage > paginationState.totalPages) {
                paginationState.currentPage = paginationState.totalPages || 1;
            }
            
            // Renderizar la página actual
            renderPage(paginationState.currentPage);
            
            // Actualizar controles de paginación
            updatePaginationControls();
        })
        .catch(error => {
            console.error('Error en la paginación:', error);
        });
}

/**
 * Renderiza una página específica
 * @param {number} page - Número de página a renderizar
 */
function renderPage(page) {
    const startIndex = (page - 1) * paginationState.recordsPerPage;
    const endIndex = Math.min(
        startIndex + paginationState.recordsPerPage, 
        paginationState.allRecords.length
    );
    const paginatedRecords = paginationState.allRecords.slice(startIndex, endIndex);
    
    const tbody = document.getElementById(paginationState.tableBodyId);
    if (!tbody) {
        console.error(`No se encontró el elemento con ID: ${paginationState.tableBodyId}`);
        return;
    }
    
    tbody.innerHTML = ''; // Limpiar contenido previo
    
    // Usar la función de callback para renderizar cada registro
    if (typeof paginationState.renderCallback === 'function') {
        paginatedRecords.forEach(record => {
            const row = paginationState.renderCallback(record);
            tbody.appendChild(row);
        });
    }
    
    // Actualizar información de paginación
    const startRecord = document.getElementById('startRecord');
    const endRecord = document.getElementById('endRecord');
    
    if (startRecord) {
        startRecord.textContent = paginationState.allRecords.length > 0 ? startIndex + 1 : 0;
    }
    
    if (endRecord) {
        endRecord.textContent = endIndex;
    }
}

/**
 * Actualiza los controles de paginación
 */
function updatePaginationControls() {
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const pageNumbers = document.getElementById('pageNumbers');
    
    if (!pageNumbers) return;
    
    // Habilitar/deshabilitar botones de navegación
    if (prevPageBtn) {
        prevPageBtn.disabled = paginationState.currentPage <= 1;
    }
    
    if (nextPageBtn) {
        nextPageBtn.disabled = paginationState.currentPage >= paginationState.totalPages;
    }
    
    // Generar números de página
    pageNumbers.innerHTML = '';
    
    const maxVisiblePages = 5;
    let startPage = Math.max(1, paginationState.currentPage - Math.floor(maxVisiblePages / 2));
    let endPage = Math.min(paginationState.totalPages, startPage + maxVisiblePages - 1);
    
    // Ajustar si estamos cerca del final
    if (endPage - startPage + 1 < maxVisiblePages && startPage > 1) {
        startPage = Math.max(1, endPage - maxVisiblePages + 1);
    }
    
    // Mostrar el primer número si hay espacio
    if (startPage > 1) {
        const firstPageBtn = createPageButton(1);
        pageNumbers.appendChild(firstPageBtn);
        
        // Añadir elipsis si hay un salto
        if (startPage > 2) {
            const ellipsis = document.createElement('span');
            ellipsis.className = 'px-2 py-1 text-gray-500';
            ellipsis.textContent = '...';
            pageNumbers.appendChild(ellipsis);
        }
    }
    
    // Generar botones de página
    for (let i = startPage; i <= endPage; i++) {
        const pageBtn = createPageButton(i);
        pageNumbers.appendChild(pageBtn);
    }
    
    // Mostrar el último número si hay espacio
    if (endPage < paginationState.totalPages) {
        // Añadir elipsis si hay un salto
        if (endPage < paginationState.totalPages - 1) {
            const ellipsis = document.createElement('span');
            ellipsis.className = 'px-2 py-1 text-gray-500';
            ellipsis.textContent = '...';
            pageNumbers.appendChild(ellipsis);
        }
        
        const lastPageBtn = createPageButton(paginationState.totalPages);
        pageNumbers.appendChild(lastPageBtn);
    }
}

/**
 * Crea un botón de página para la paginación
 * @param {number} pageNum - Número de página
 * @returns {HTMLButtonElement} - Elemento botón creado
 */
function createPageButton(pageNum) {
    const button = document.createElement('button');
    button.textContent = pageNum;
    button.className = 'px-3 py-1 rounded text-sm';
    
    if (pageNum === paginationState.currentPage) {
        button.className += ' bg-zinc-800 text-white';
    } else {
        button.className += ' border border-gray-300 bg-white text-gray-700 hover:bg-gray-100';
    }
    
    button.addEventListener('click', () => {
        if (pageNum !== paginationState.currentPage) {
            paginationState.currentPage = pageNum;
            renderPage(paginationState.currentPage);
            updatePaginationControls();
        }
    });
    
    return button;
}

/**
 * Refresca los datos y mantiene la página actual
 */
function refreshPagination() {
    fetchRecords();
}

// Exportar funciones para uso global
window.paginationController = {
    init: initPagination,
    refresh: refreshPagination,
    goToPage: (page) => {
        paginationState.currentPage = page;
        renderPage(page);
        updatePaginationControls();
    },
    getPageInfo: () => ({
        currentPage: paginationState.currentPage,
        totalPages: paginationState.totalPages,
        recordsPerPage: paginationState.recordsPerPage,
        totalRecords: paginationState.allRecords.length
    })
};