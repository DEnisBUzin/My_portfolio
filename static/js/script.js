// Ключ для хранения задач в localStorage
const STORAGE_KEY = 'tasks';

// Инициализация задач из localStorage
document.addEventListener('DOMContentLoaded', () => {
    const tasks = loadTasks();
    renderTasks(tasks);
});

// Добавление новой задачи
document.querySelectorAll('.add-task').forEach(button => {
    button.addEventListener('click', () => {
        const taskText = prompt('Введите описание задачи:');
        if (taskText) {
            const columnId = button.parentElement.id; // Получаем ID колонки (todo, in-progress, done)
            const tasks = loadTasks();
            tasks.push({ text: taskText, status: columnId });
            saveTasks(tasks);
            renderTasks(tasks);
        }
    });
});

// Функция для загрузки задач из localStorage
function loadTasks() {
    const tasksJSON = localStorage.getItem(STORAGE_KEY);
    return tasksJSON ? JSON.parse(tasksJSON) : [];
}

// Функция для сохранения задач в localStorage
function saveTasks(tasks) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

// Функция для отрисовки задач на странице
function renderTasks(tasks) {
    // Очищаем предыдущий список задач
    document.querySelectorAll('.task-list').forEach(list => list.innerHTML = '');

    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.textContent = task.text;
        taskItem.classList.add('task-item');
        taskItem.addEventListener('click', () => {
            if (confirm('Удалить задачу?')) {
                const updatedTasks = tasks.filter(t => t !== task);
                saveTasks(updatedTasks);
                renderTasks(updatedTasks);
            }
        });

        // Добавляем задачу в соответствующую колонку
        const column = document.querySelector(`#${task.status} .task-list`);
        if (column) column.appendChild(taskItem);
    });
}
