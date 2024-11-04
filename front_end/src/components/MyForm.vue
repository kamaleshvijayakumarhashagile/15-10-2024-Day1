<template>
    <div class="app-container">
        <header class="header">
            <img src="../assets/HashAgile.png" alt="Logo" class="logo" />
            <nav class="nav">
                <ul>
                    <li><a href="#" @click.prevent="showHomeContent">Home</a></li>
                    <li><a href="#" @click.prevent="showUploadForm">AI Recruiter</a></li>
                </ul>
            </nav>
        </header>
        <div class="content">
            <div v-if="showHome">
                <h2>Welcome to Hashagile</h2>
                <p>Hasagile is located in Coimbatore with a team of 150 dedicated employees. We specialize in providing
                    top-notch recruitment solutions to meet your needs.</p>
            </div>
            <div v-else>
                <div class="form-container">
                    <h2>AI Recruiter</h2>
                    <form @submit.prevent="handleSubmit">
                        <div class="form-group"><label for="resume">Upload Resume:</label> <input type="file"
                                @change="handleFileUpload" id="resume" accept=".pdf,.doc,.docx" required /></div>
                        <div class="form-group"><label for="firstName">First Name:</label> <input
                                v-model="formData.first_name" type="text" id="firstName"
                                placeholder="Enter your Firstname" required /></div>
                        <div class="form-group"><label for="lastName">Last Name:</label> <input
                                v-model="formData.last_name" type="text" id="lastName" placeholder="Enter your Lastname"
                                required /></div>
                        <div class="form-group"><label for="email">Email:</label> <input v-model="formData.email"
                                type="email" id="email" placeholder="example@mail.com" required /></div>
                        <div class="form-group"><label for="phone">Phone No:</label> <input v-model="formData.phone_no"
                                type="tel" id="phone" placeholder="Enter phone number" maxlength="10" required
                                @keypress="validateNumber" /></div>
                        <div class="form-group"><label for="experience">Years of Experience:</label> <input
                                v-model="formData.experience" type="number" id="experience"
                                placeholder="Experience in years" min="0" required @keypress="validateNumber" /></div>
                        <div class="form-group"><label for="internshipExperience">Internship Experience:</label> <input
                                v-model="formData.internship_experience" type="number" id="internshipExperience"
                                placeholder="Internship experience in months" min="0" required
                                @keypress="validateNumber" /></div>
                        <div class="form-group"><label for="noticePeriod">Notice Period:</label> <input
                                v-model="formData.notice_period" type="text" id="noticePeriod" placeholder="In days"
                                required @keypress="validateNumber" /></div>
                        <div class="form-group"><label for="education">Degree:</label> <input
                                v-model="formData.education" type="text" id="education" placeholder="Enter your degree"
                                required /></div>
                        <div class="form-group"><label for="yearPassing">Year of Passing:</label> <select
                                v-model="formData.year_of_passing" id="yearPassing" required>
                                <option value="" disabled>Select Year</option>
                                <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
                            </select></div>
                        <div class="form-group"><label for="college">College:</label> <input v-model="formData.college"
                                type="text" id="college" placeholder="College name" required /></div>
                        <div class="form-group"><label for="skills">Skills:</label> <input v-model="formData.skills"
                                type="text" id="skills" placeholder="List your skills (comma-separated)" required />
                        </div>
                        <div class="form-group"><label for="location">Location:</label> <input
                                v-model="formData.location" type="text" id="location" placeholder="Address" required />
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MyFormComponent',
    data() {
        return {
            showHome: true,
            formData: {
                first_name: '',
                last_name: '',
                email: '',
                phone_no: '',
                experience: '',
                internship_experience: '',
                notice_period: '',
                education: '',
                year_of_passing: '',
                college: '',
                skills: '',
                location: '',
            },
            years: Array.from({ length: 20 }, (_, i) => new Date().getFullYear() + 2 - i), // Last 20 years
        };
    },
    methods: {
        showHomeContent() {
            this.showHome = true;
        },
        showUploadForm() {
            this.showHome = false;
        },
        validateNumber(event) {
            const char = String.fromCharCode(event.charCode);
            if (!/[0-9]/.test(char) && event.charCode !== 0) { // Allow backspace
                event.preventDefault();
            }
        },
        async handleSubmit() {
            const dataToSend = [this.formData]; // Wrap formData in an array
            try {
                const response = await fetch('http://localhost:5000/load', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataToSend),
                });
                if (response.ok) {
                    this.displayMessage('Data submitted successfully!', 'success');
                    this.resetForm();
                } else {
                    const errorResponse = await response.json();
                    this.displayMessage(`Error: ${errorResponse.error}`, 'error');
                }
            } catch (error) {
                console.error('Submission error:', error);
                this.displayMessage('Error submitting data. Please try again.', 'error');
            }
        },
        displayMessage(message, type) {
            const messageDiv = document.createElement('div');
            messageDiv.textContent = message;
            messageDiv.classList.add('message-box', type);
            document.body.appendChild(messageDiv);
            setTimeout(() => {
                messageDiv.classList.add('fade-out');
            }, 2500);
            setTimeout(() => {
                messageDiv.remove();
            }, 3000);
        },
        resetForm() {
            this.formData = {
                first_name: '',
                last_name: '',
                email: '',
                phone_no: '',
                experience: '',
                internship_experience: '',
                notice_period: '',
                education: '',
                year_of_passing: '',
                college: '',
                skills: '',
                location: '',
            };
        },
    },
};
</script>

<style scoped>
.app-container {
  text-align: center;
  padding: 0;
}
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #f8f9fa;
}
.logo {
  width: 350px;
}
.nav ul {
  list-style-type: none;
  display: flex;
  margin: 0;
  padding: 0;
}
.nav li {
  margin-left: 20px;
}
.nav a {
  text-decoration: none;
  color: #007bff;
}
.nav a:hover {
  text-decoration: underline;
}
.content {
  padding: 20px;
}
.form-container {
  max-width: 600px;
  margin: auto;
}
form {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 10px;
  align-items: center;
}
.form-group {
  display: contents;
}
label {
  text-align: right;
  margin-bottom: 5px;
}
input, select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  grid-column: 2 / 3;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #218838;
}
.message {
  margin-top: 20px;
  font-size: 1.2em;
  color: green; /* Adjust color as needed */
}
</style>
