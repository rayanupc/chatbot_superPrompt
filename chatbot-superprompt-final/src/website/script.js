const chatInput = document.querySelector("#chat-input");
const sendButton = document.querySelector("#send-btn");
const chatContainer = document.querySelector(".chat-container");
const themeButton = document.querySelector("#theme-btn");
const deleteButton = document.querySelector("#delete-btn");
const uploadFileButton = document.querySelector("#upload-file-btn");
const uploadFileTooltip = document.querySelector("#upload-file-tooltip");
const apikeyInput = document.querySelector("#chatgpt-apikey");
const selectLLM = document.querySelector("#llm-type");
const selectRAG = document.querySelector("#rag-type");
const selectEnrichment = document.querySelector("#enrichment-type");
const secureModeBox = document.querySelector("#secure-mode");
const fileInput = document.querySelector(".file-input");
const archiveAddButton = document.querySelector(".archive-add-btn");
const archiveContainer = document.querySelector(".archive-container");

// localStorage.clear();

var storage = [];
var messages = [];
let themeColor = "light-mode";
let nb_archive = 1;
let archiveNumber = 1;

let files = [];
let userText = null;

const userName = "Utilisateur";
const chatbotName = "AI";

const API_KEY = "PASTE-YOUR-API-KEY-HERE";
const LOCAL_SERVER = "http://127.0.0.1:5000/";

const DEFAULT_TEXT_HTML = `
    <h1>ChatBot SuperPrompt</h1>
    <h3>New chat</h3>
    <p>Use the Chatbot SuperPrompt to enhance prompts and select the best answers from among many language models!</p>
`;

const SPAN_BUTTONS_HTML = `
    <div class="span-buttons">
        <span onclick="copyResponse(this)" title="Copier le texte de la réponse" class="material-symbols-rounded">content_copy</span>
        <span onclick="regenerateResponse(this)" data-value="temperature" title="Changer la temperature de la réponse pour la rendre plus détaillée" class="material-symbols-rounded">thermometer_minus</span>
        <span onclick="regenerateResponse(this)" data-value="top-p" title="Changer le top-p de la réponse pour la rendre plus précise" class="material-symbols-rounded">replay</span>
    </div>`


/* Every fonctions */

const displayContentFromStorage = () => {
    console.log("displayContentFromStorage(): ");
    console.log("archiveNumber", archiveNumber);
    console.log("storage", storage);
    // Load saved chats, messages
    chatContainer.innerHTML = storage[archiveNumber-1]["chat-content"];
    messages = storage[archiveNumber-1]["messages"];
    
    chatContainer.scrollTo(0, chatContainer.scrollHeight); // Scroll to bottom of the chat container
}

const initLoadFromStorage = () => {
    // Load storage
    const defaultText = `<div class="default-text">
                            ${DEFAULT_TEXT_HTML}
                    </div>`;

    // Initialisation & Loading local storage content
    storage = JSON.parse(localStorage.getItem("chabotsuperprompt-storage") || "[]");
    if (storage.length === 0) storage.push({"archive-name":"Chat 1", "messages":[{"role":"system","content":"You are a helpfull assistant"}], "chat-content":defaultText});
    
    // Load themeColor
    themeColor = localStorage.getItem("themeColor");
    document.body.classList.toggle("light-mode", themeColor === "light_mode");
    themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
    
    // Load archiveContainer
    reloadArchiveButtons();
    
    // Select the button 1
    archiveNumber = 1;
    const archiveButton1 = document.querySelector("#archive-btn-1");
    archiveButtonSelection(archiveButton1);
}

const reloadArchiveButtons = () => {
    nb_archive = storage.length;
    archiveContainer.innerHTML = ""
    for (let i = 0; i < storage.length; i++) {
        archiveContainer.innerHTML += `<div id="archive-btn-${i+1}" class="archive" onclick="archiveButtonSelection(this)">
                                            ${storage[i]["archive-name"]}
                                        </div>`
    }
}

const saveDataFromLocalstorage = () => {
    // Storage save
    storage[archiveNumber-1]["chat-content"] = chatContainer.innerHTML;
    localStorage.setItem("chabotsuperprompt-storage", JSON.stringify(storage));
    // Light mode save
    localStorage.setItem("themeColor", themeColor);
}

const createChatElement = (content, className) => {
    // Create new div and apply chat, specified class and set html content of div
    const chatDiv = document.createElement("div");
    chatDiv.classList.add("chat", className);
    chatDiv.innerHTML = content;
    return chatDiv; // Return the created chat div
}

const getChatResponse = async (incomingChatDiv) => {
    const API_URL = LOCAL_SERVER + "chatbot";
    const divChatText = document.createElement("div");
    divChatText.classList.add("chat-text");
    
    var formData = new FormData();
    let title = null;

    // Put the properties and data in a 'FormData' format (for file management)
    formData.append("prompt", userText);
    formData.append("enrichment_type", selectEnrichment.value);
    formData.append("llm_type", selectLLM.value);
    formData.append("rag_type", selectRAG.value);
    formData.append("apikey", apikeyInput.value.trim());
    formData.append("secure_mode", secureModeBox.checked); // True if "checked"
    formData.append("messages", JSON.stringify(messages));
    Array.from(files).forEach(file => formData.append("files", file)); // list of files

    // Define the properties and data for the API request
    const requestOptions = {
        method: 'POST',
        body: formData,
    };

    // Send POST request to API, get response, set the reponse as paragraph element text and as a json 'messages'
    try {
        const response = await fetch(API_URL, requestOptions);
        const data = await response.json();
        // Verify the response status
        if (!response.ok) {
          throw new Error(data.error);
        }
        const responseText = data.response.trim();
        const modelText = data.model.trim();
        const augmentPromptText = data.context.trim();
        console.log("context:\n ", augmentPromptText);
        
        // Update messages chat for api request
        const userMessage = {"role": "user", "content": userText};
        messages.push(userMessage);
        const responseMessage = {"role": "assistant", "content": responseText};
        messages.push(responseMessage);
        
        // Update chat html text
        const html = `
            <p class="chatbotname-headline">${chatbotName} ${modelText}</p>
            <p class="text">${responseText}</p>
            ${SPAN_BUTTONS_HTML}
        `;
        divChatText.innerHTML = html;
        
        // Create the enriched prompt
        const outgoingChatDiv = incomingChatDiv.previousElementSibling;
        if (augmentPromptText.length !== 0){
            const chatTextElement = outgoingChatDiv.querySelector(".chat-text");
            const html = `<div class="enriched-prompt">
                                <p class="enriched-prompt-headline">Prompt enrichi</p>
                                <p class="enriched-prompt-text-hide">${augmentPromptText}</p>
                            </div>
                            <span onclick="showEnrichedPrompt(this)" class="material-symbols-rounded">expand_all</span>`;
            chatTextElement.children[1].insertAdjacentHTML('afterend', html); // Inser 'html' after the username
        }

        // Update info for the title
        title = responseText;

    } catch (error) {
        let errorText = "Oops! Something went wrong while retrieving the response. Please try again.";
        if (error.message.substring(0, 5) === "Oops!") errorText = error.message;
        const html = `<p class="error">${errorText}</p>`;
        console.log(error);
        divChatText.innerHTML = html;
        title = null;
    }
    // Remove the typing animation, append the paragraph element, save the chats and messages to local storage and upload file icon
    incomingChatDiv.querySelector(".typing-animation").remove();
    const chatDetailsElement = incomingChatDiv.querySelector(".chat-details");
    chatDetailsElement.appendChild(divChatText);

    // Update the display of temperature and top-p options
    var event = new Event('change', {
        bubbles: true,
        cancelable: true,
    });
    apikeyInput.dispatchEvent(event);
    
    // Put upload file button and icon to default
    fileInput.value = null;
    uploadFileButton.innerText = "upload_file";
    uploadFileTooltip.innerText = "Upload Files Here";

    // Create a title for the default archive name
    archiveName = storage[archiveNumber-1]["archive-name"];
    if (archiveName.includes("Chat") && archiveName.length === 6 && title !== null && title !== "") getTitle(title);

    saveDataFromLocalstorage();
    chatContainer.scrollTo(0, chatContainer.scrollHeight);
}

const getTitle = async (text) => {
    const API_URL = LOCAL_SERVER + "title";
    var formData = new FormData();

    formData.append("text", text);

    // Define the properties and data for the API request
    const requestOptions = {
        method: 'POST',
        body: formData,
    };

    try{
        const data = await (await fetch(API_URL, requestOptions)).json();
        const title = data.response;
        storage[archiveNumber-1]["archive-name"] = title;
    } catch (error) {
        console.log(error);
    }
    // Display the new title
    const archiveButtonCurrent = document.querySelector(`#archive-btn-${archiveNumber}`);
    archiveButtonCurrent.innerText = storage[archiveNumber-1]["archive-name"];
    // Save the new title in the storage
    saveDataFromLocalstorage();
}

const regenerateResponse = (regenerateButton) => {
    // Selected option
    const option = regenerateButton.getAttribute('data-value');
    const previousResponse = regenerateButton.parentElement.parentElement.querySelector(".text").textContent;
    console.log("regenerateResponse():");
    console.log("regenerateButton.parentElement:", regenerateButton.parentElement);
    console.log("previousResponse:", previousResponse);
    setTimeout(showTypingAnimation(option, previousResponse), 500);
}

const getRegenerateResponse = async (incomingChatDiv, option, previousResponse) => {
    const divChatText = document.createElement("div");
    divChatText.classList.add("chat-text");

    // Send POST request to API
    const API_URL = LOCAL_SERVER + "regenerate";
    var formData = new FormData();

    formData.append("prompt", userText);
    formData.append("regenerate_option", option);
    formData.append("response", previousResponse);
    formData.append("apikey", apikeyInput.value.trim());

    // Define the properties and data for the API request
    const requestOptions = {
        method: 'POST',
        body: formData,
    };

    try {
        const data = await (await fetch(API_URL, requestOptions)).json();
        const newReponseText = data.response.trim();
        const modelText = data.model.trim(); 

        // Update messages chat for api request
        messages.pop();
        const responseMessage = {"role": "assistant", "content": newReponseText};
        messages.push(responseMessage);
        
        // Update chat html text
        const html = `
            <p class="chatbotname-headline">${chatbotName} ${modelText}</p>
            <p class="text">${newReponseText}</p>
            ${SPAN_BUTTONS_HTML}
        `;
        divChatText.innerHTML = html;

    } catch (error) {
        let errorText = "Oops! Something went wrong while retrieving the response. Please try again.";
        if (error.message.substring(0, 5) === "Oops!") errorText = error.message;
        const html = `<p class="error">${errorText}</p>`;
        console.log(error);
        divChatText.innerHTML = html;
    }
    // Remove the typing animation, append the paragraph element, save the chats and messages to local storage and upload file icon
    incomingChatDiv.querySelector(".typing-animation").remove();
    const chatDetailsElement = incomingChatDiv.querySelector(".chat-details");
    chatDetailsElement.appendChild(divChatText);

    // Update the display of temperature and top-p options
    var event = new Event('change', {
        bubbles: true,
        cancelable: true,
    });
    apikeyInput.dispatchEvent(event);

    saveDataFromLocalstorage();
    chatContainer.scrollTo(0, chatContainer.scrollHeight);


}

const copyResponse = (copyButton) => {
    // Copy the text content of the response to the clipboard
    const responseTextElement = copyButton.parentElement.parentElement.querySelector(".text");
    navigator.clipboard.writeText(responseTextElement.textContent);
    copyButton.textContent = "done";
    setTimeout(() => copyButton.textContent = "content_copy", 1000);
}

const showEnrichedPrompt = (enrichedPromptButton) => {
    const enrichedTextElement = enrichedPromptButton.parentElement.querySelector(".enriched-prompt-headline").nextElementSibling;
    if (enrichedTextElement.className === "enriched-prompt-text"){
        enrichedTextElement.className = "enriched-prompt-text-hide"; 
        enrichedPromptButton.innerHTML = "expand_all";
    }else if (enrichedTextElement.className === "enriched-prompt-text-hide"){
        enrichedTextElement.className = "enriched-prompt-text";
        enrichedPromptButton.innerHTML = "collapse_all";
    }
}

const showTypingAnimation = (regenerateOption=null, previousResponse=null) => {
    // Display the typing animation and call the getChatResponse function
    const html = `<div class="chat-content">
                    <div class="chat-details">
                        <img src="images/chatbot.jpg" alt="chatbot-img" width="89" height="89">
                        <div class="typing-animation">
                            <div class="typing-dot" style="--delay: 0.2s"></div>
                            <div class="typing-dot" style="--delay: 0.3s"></div>
                            <div class="typing-dot" style="--delay: 0.4s"></div>
                        </div>
                    </div>
                </div>`;
    // Create an incoming chat div with typing animation and append it to chat container
    const incomingChatDiv = createChatElement(html, "incoming");
    chatContainer.appendChild(incomingChatDiv);
    chatContainer.scrollTo(0, chatContainer.scrollHeight);
    if (regenerateOption === null) getChatResponse(incomingChatDiv);
    else getRegenerateResponse(incomingChatDiv, regenerateOption, previousResponse);
}

const handleOutgoingChat = () => {
    userText = chatInput.value.trim(); // Get chatInput value and remove extra spaces
    if (!userText) return; // If chatInput is empty return from here

    // Clear the input field and reset its height
    chatInput.value = "";
    chatInput.style.height = `${initialInputHeight}px`;

    const html = `<div class="chat-content">
                    <div class="chat-details">
                        <img src="images/user.jpg" alt="user-img" width="89" height="89">
                        <div class="chat-text">
                            <p class="username-headline">${userName}</p>
                            <p>${userText}</p>
                        </div>
                    </div>
                </div>`;

    // Create an outgoing chat div with user's message and append it to chat container
    const outgoingChatDiv = createChatElement(html, "outgoing");
    chatContainer.querySelector(".default-text")?.remove();
    chatContainer.appendChild(outgoingChatDiv);
    chatContainer.scrollTo(0, chatContainer.scrollHeight);
    setTimeout(showTypingAnimation, 500);
}

const archiveButtonDeselection = () => {
    const archiveButtonSelected = document.querySelector(".archive-btn-selected");
    if (archiveButtonSelected !== null)
        archiveButtonSelected.className = "archive-btn";
}

const archiveButtonSelection = (archiveButton) => {
    archiveButtonDeselection();
    const archiveButtonId = archiveButton.id;
    archiveNumber = parseInt(archiveButtonId.charAt(archiveButtonId.length - 1));
    archiveButton.className = "archive-btn-selected";
    displayContentFromStorage();
}

initLoadFromStorage();


/* Every addEventListener */

deleteButton.addEventListener("click", () => {
    // Remove the chats from local storage and call displayContentFromStorage function
    const nombreDeChildDiv = archiveContainer.childElementCount;
    if (nombreDeChildDiv > 1){
        if (confirm("Are you sure you want to delete the current chat?")){
            storage.splice(archiveNumber-1, 1);
            const archiveButtonDelete = document.querySelector(`#archive-btn-${archiveNumber}`);
            archiveContainer.removeChild(archiveButtonDelete);
            nb_archive = storage.length;
            reloadArchiveButtons();
            const archiveButtonOne = document.querySelector("#archive-btn-1");
            archiveButtonOne.click();
            saveDataFromLocalstorage();
        }
    }
    else {
        alert("Oops! There is only one archive left. You can not delete it :(")
    }
});

themeButton.addEventListener("click", () => {
    // Toggle body's class for the theme mode and save the updated theme to the local storage 
    document.body.classList.toggle("light-mode");
    localStorage.setItem("themeColor", themeButton.innerText);
    themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
});

uploadFileButton.addEventListener("click", () => {
    fileInput.click();
    if (uploadFileButton.innerText === "download_done")
        uploadFileButton.innerText = "upload_file";
});

fileInput.addEventListener("change", () => {
    files = fileInput.files;
    uploadFileButton.innerText = "download_done";
    uploadFileTooltip.innerText = "";
    Array.from(files).forEach(file => uploadFileTooltip.textContent += "\n" + file.name)
});

const initialInputHeight = chatInput.scrollHeight;
chatInput.addEventListener("input", () => {
    // Adjust the height of the input field dynamically based on its content
    chatInput.style.height = `${initialInputHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (event) => {
    // If the Enter key is pressed without Shift and the window width is larger 
    // than 800 pixels, handle the outgoing chat
    if (event.key === "Enter" && !event.shiftKey && window.innerWidth > 800) {
        event.preventDefault();
        handleOutgoingChat();
    }
});

sendButton.addEventListener("click", handleOutgoingChat);

chatInput.addEventListener("keypress", (event) => {
    if (event.key === 'Enter') {
        handleOutgoingChat();
    }
});

archiveAddButton.addEventListener("click", () => {
    const defaultText = `<div class="default-text">
                            ${DEFAULT_TEXT_HTML}
                    </div>`;
    storage.push({
        "archive-name":`Chat ${nb_archive+1}`, 
        "messages":[{"role":"system","content":"You are a helpfull assistant"}], 
        "chat-content":`${defaultText}`
    });

    nb_archive = storage.length;
    archiveNumber = nb_archive;
    archiveContainer.innerHTML += `<div id="archive-btn-${archiveNumber}" class="archive-btn-selected" onclick="archiveButtonSelection(this)">
                                        ${storage[archiveNumber-1]["archive-name"]}
                                    </div>`;
    const archiveButtonCurrent = document.querySelector(`#archive-btn-${archiveNumber}`);
    archiveButtonSelection(archiveButtonCurrent);
    saveDataFromLocalstorage();

    const archiveBox = document.querySelector(".archive");
    archiveBox.scrollTo(0, archiveBox.scrollHeight);
});

apikeyInput.addEventListener("change", () => {
    const option1 = selectEnrichment.querySelector('option[value="llm-chatgpt"]');
    const option2 = selectRAG.querySelector('option[value="internet"]');
    const option3 = selectRAG.querySelector('option[value="pdf"]');
    const option4 = selectLLM.querySelector('option[value="chatgpt"]');
    const temperatureOptions = chatContainer.querySelectorAll('span[data-value="temperature"]');
    const topPOptions = chatContainer.querySelectorAll('span[data-value="top-p"]');

    if (apikeyInput.value !== ''){
        option1.disabled = false; option2.disabled = false; option3.disabled = false; option4.disabled = false;
        Array.from(temperatureOptions).forEach(temperatureOption => temperatureOption.style.display = 'inline');
        Array.from(topPOptions).forEach(temperatureOption => temperatureOption.style.display = 'inline');
    }else{
        option1.disabled = true; option2.disabled = true; option3.disabled = true; option4.disabled = true;
        Array.from(temperatureOptions).forEach(temperatureOption => temperatureOption.style.display = 'none');
        Array.from(topPOptions).forEach(temperatureOption => temperatureOption.style.display = 'none');
    }
});

selectRAG.addEventListener("change", () => {
    if (selectRAG.value === "pdf") {
        uploadFileButton.style.display = 'flex';
    } else {
        uploadFileButton.style.display = 'none';
    }
});