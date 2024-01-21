const navbar = document.querySelector('.navbar');
const toggleButton = document.getElementById('navbar-toggle-button');

toggleButton.addEventListener('click', () => {
    console.log('Slide-out button clicked!');  
    navbar.classList.toggle('slide-out');  
});

const slideInButton = document.getElementById('navbar-slide-in-button');

navbar.addEventListener('transitionend', () => {
    slideInButton.classList.toggle('hidden', navbar.classList.contains('slide-out'));
});

slideInButton.addEventListener('click', () => {
    navbar.classList.toggle('slide-out');
});

function fetchFirmsInfo() {
    var firmsInfoContainer = document.getElementById('firmsInfoContainer');

    if (firmsInfoContainer) {
        fetch('/get_firms_info')
            .then(response => response.text())
            .then(data => {
                console.log('Received data:', data);

                const firmsArray = data.split(' ');

                const firmsList = firmsArray.map(item => `<li>${item}</li>`).join('');
                const newContent = `<ul>${firmsList}</ul>`;
                firmsInfoContainer.innerHTML = newContent;
            })
            .catch(error => console.error('Error fetching data:', error));
    } else {
        console.error('firmsInfoContainer not found');
    }
}

const navbarScrollContainer = document.querySelector('.navbar-scroll-container');
const navbarLinks = navbarScrollContainer.querySelectorAll('.navbar-nav li');

let totalWidth = 0;
navbarLinks.forEach(link => {
    totalWidth += link.offsetWidth;
});

navbarScrollContainer.style.width = totalWidth + 'px';

document.addEventListener('DOMContentLoaded', function () {
    let businessData = [];

    function updateBusinessDetails(index, field, value) {
        if (businessData[index]) {
            businessData[index][field] = value;
        } else {
            console.error(`Invalid index ${index} in updateBusinessDetails`);
        }
    }

    function updateTaskDetails(index, taskIndex, field, value) {
        if (businessData[index] && businessData[index].tasks[taskIndex]) {
            businessData[index].tasks[taskIndex][field] = value;
        } else {
            console.error(`Invalid index or taskIndex in updateTaskDetails`);
        }
    }

    function updateRevenueDetails(index, field, value) {
        businessData[index].revenue[field] = value;
    }

    function createBusiness() {
        return {
            name: '',
            location: '',
            industry: '',
            revenue: {
                annual: '',
                monthly: '',
            },
            tasks: [],
        };
    }

    function renderBusinessDetails(business, index) {
        clearContainers();

        const businessDetailsForm = createBusinessDetailsForm(business, index);
        businessDetailsContainer.appendChild(businessDetailsForm);

        const revenueDetailsForm = createRevenueDetailsForm(business, index);
        revenueDetailsContainer.appendChild(revenueDetailsForm);

        attachInputEventListeners(index);
        renderTasksExpensesForm(business, index);
    }

    function attachInputEventListeners(index) {
        const businessNameInput = document.getElementById(`business-name-${index}`);
        const businessLocationInput = document.getElementById(`business-location-${index}`);
        const businessIndustryInput = document.getElementById(`business-industry-${index}`);
        const annualRevenueInput = document.getElementById(`annual-revenue-${index}`);
        const monthlyRevenueInput = document.getElementById(`monthly-revenue-${index}`);

        businessNameInput.addEventListener('input', function () {
            updateBusinessDetails(index, 'name', businessNameInput.value);
        });

        businessLocationInput.addEventListener('input', function () {
            updateBusinessDetails(index, 'location', businessLocationInput.value);
        });

        businessIndustryInput.addEventListener('input', function () {
            updateBusinessDetails(index, 'industry', businessIndustryInput.value);
        });

        annualRevenueInput.addEventListener('input', function () {
            updateRevenueDetails(index, 'annual', annualRevenueInput.value);
        });

        monthlyRevenueInput.addEventListener('input', function () {
            updateRevenueDetails(index, 'monthly', monthlyRevenueInput.value);
        });
    }

    function renderSavedBusinessData(businessData) {
        savedBusinessDataContainer.innerHTML = '';

        businessData.forEach((business, index) => {
            const businessDataContainer = document.createElement('div');

            const savedBusinessData = createSavedBusinessData(business, index);
            businessDataContainer.appendChild(savedBusinessData);

            savedBusinessDataContainer.appendChild(businessDataContainer);

            const tasksExpensesForm = createTasksExpensesForm(business, index);
            tasksExpensesContainer.appendChild(tasksExpensesForm);
        });
    }

    function clearContainers() {
        businessDetailsContainer.innerHTML = '';
        revenueDetailsContainer.innerHTML = '';
        tasksExpensesContainer.innerHTML = '';
    }

    function createBusinessDetailsForm(business, index) {
        const form = document.createElement('div');
        form.innerHTML = `
            <p><strong>Business Name:</strong> <input type="text" id="business-name-${index}" value="${business.name || ''}" oninput="updateBusinessDetails(${index}, 'name', this.value)"></p>
            <p><strong>Location:</strong> <input type="text" id="business-location-${index}" value="${business.location || ''}" oninput="updateBusinessDetails(${index}, 'location', this.value)"></p>
            <p><strong>Industry:</strong> <input type="text" id="business-industry-${index}" value="${business.industry || ''}" oninput="updateBusinessDetails(${index}, 'industry', this.value)"></p>
        `;
        return form;
    }

    function createRevenueDetailsForm(business, index) {
        const form = document.createElement('div');
        form.innerHTML = `
            <p><strong>Annual Revenue:</strong> $<input type="text" id="annual-revenue-${index}" value="${business.revenue.annual || ''}" oninput="updateRevenueDetails(${index}, 'annual', this.value)"></p>
            <p><strong>Monthly Revenue:</strong> $<input type="text" id="monthly-revenue-${index}" value="${business.revenue.monthly || ''}" oninput="updateRevenueDetails(${index}, 'monthly', this.value)"></p>
        `;
        return form;
    }

    function createTasksExpensesForm(business, index) {
        const form = document.createElement('div');
        const tasksList = document.createElement('ul');

        business.tasks.forEach((task, taskIndex) => {
            const taskItem = document.createElement('li');
            taskItem.innerHTML = `
                <strong>Task ${taskIndex + 1}:</strong> Description: 
                <input type="text" id="task${taskIndex + 1}-description-${index}" value="${task.description || ''}" oninput="updateTaskDetails(${index}, ${taskIndex}, 'description', this.value)"> 
                Cost: $<input type="text" id="task${taskIndex + 1}-cost-${index}" value="${task.cost || ''}" oninput="updateTaskDetails(${index}, ${taskIndex}, 'cost', this.value)">
            `;

            tasksList.appendChild(taskItem);
        });

        form.appendChild(tasksList);

        const addTaskButton = document.createElement('button');
        addTaskButton.innerHTML = 'Add Task';
        addTaskButton.addEventListener('click', function () {
            business.tasks.push({ description: '', cost: '' });
            renderTasksExpensesForm(business, index);
        });
        form.appendChild(addTaskButton);

        return form;
    }

    function renderTasksExpensesForm(business, index) {
        const tasksExpensesForm = createTasksExpensesForm(business, index);
        tasksExpensesContainer.innerHTML = '';
        tasksExpensesContainer.appendChild(tasksExpensesForm);
    }

    function createSavedBusinessData(business, index) {
        const savedBusinessData = document.createElement('div');
        savedBusinessData.innerHTML = `
            <p><strong>Business Name:</strong> <span>${business.name}</span></p>
            <p><strong>Location:</strong> <span>${business.location}</span></p>
            <p><strong>Industry:</strong> <span>${business.industry}</span></p>
            <p><strong>Annual Revenue:</strong> $<span>${business.revenue.annual}</span></p>
            <p><strong>Monthly Revenue:</strong> $<span>${business.revenue.monthly}</span></p>
            <p><strong>Tasks/Expenses:</strong></p>
        `;
    
        const tasksListContainer = document.createElement('ul');
        business.tasks.forEach((task, taskIndex) => {
            const taskItem = document.createElement('li');
            taskItem.innerHTML = `
                <span>Task ${taskIndex + 1}:</span> Description - ${task.description}, Cost - $${task.cost}
            `;
            tasksListContainer.appendChild(taskItem);
        });
    
        savedBusinessData.appendChild(tasksListContainer);
    
        const editButton = document.createElement('button');
        editButton.innerHTML = 'Edit';
        editButton.addEventListener('click', function () {
            editBusinessData(index);
        });
    
        savedBusinessData.appendChild(editButton);
    
        return savedBusinessData;
    }

    // Example: Accessing elements by ID
    const addBusinessButton = document.getElementById('add-business-button');
    const submitBusinessButton = document.getElementById('submit-business-button');
    const toggleBusinessSectionButton = document.getElementById('toggle-business-section-button');
    const businessSections = ['business-info', 'revenue', 'tasks-expenses'];
    const businessDetailsContainer = document.getElementById('business-details-container');
    const revenueDetailsContainer = document.getElementById('revenue-details-container');
    const tasksExpensesContainer = document.getElementById('tasks-expenses-container');
    const savedBusinessDataContainer = document.getElementById('saved-business-data-container');

    addBusinessButton.addEventListener('click', function () {
        const business = createBusiness();
        businessData.push(business);
        renderBusinessDetails(business, businessData.length - 1);
    });

    submitBusinessButton.addEventListener('click', function () {
        renderSavedBusinessData(businessData);
    });

    toggleBusinessSectionButton.addEventListener('click', function () {
        businessSections.forEach(sectionId => {
            const element = document.getElementById(sectionId);
            element.style.display = element.style.display === 'none' || element.style.display === '' ? 'block' : 'none';
        });
    });

    window.editBusinessData = function (index) {
        const business = businessData[index];
        renderBusinessDetails(business, index);
    };

    // ... (existing code for quiz game)

    function handleNextButtonClick() {
        fetch('/next_level')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const options = data.options || [];
                console.log('Response data:', data);

                if (data.enable_next) {
                    updateUIForNextLevel({ ...data, options });
                } else {
                    console.log('Game Over');
                    // You can provide a message or redirect to another page for game over
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle error gracefully, e.g., show an error message to the user
            });
    }

    function updateUIForNextLevel(data) {
        document.getElementById('label-instruction').textContent = data.description;

        const optionsContainer = document.getElementById('options-container');
        optionsContainer.innerHTML = '';

        data.options.forEach(option => {
            const button = createOptionButton(option);
            optionsContainer.appendChild(button);
        });

        document.getElementById('nextButton').disabled = true;
        document.getElementById('answer-feedback').textContent = '';
    }

    document.getElementById('nextButton').addEventListener('click', handleNextButtonClick);
});
