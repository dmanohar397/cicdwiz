let workflowData = ""
let dockerData = ""

async function generatePipeline(){

const data = {

repo: document.getElementById("repo").value,
language: document.getElementById("language").value,
framework: document.getElementById("framework").value,
docker: true,
cloud: document.getElementById("cloud").value

}

const response = await fetch("http://127.0.0.1:8000/generate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})

const result = await response.json()

workflowData = result.workflow
dockerData = result.dockerfile

document.getElementById("output").textContent =
workflowData + "\n\n" + dockerData

}

function downloadWorkflow(){

const blob = new Blob([workflowData], {type:"text/plain"})
const url = URL.createObjectURL(blob)

const a = document.createElement("a")
a.href = url
a.download = "workflow.yml"
a.click()

}

function downloadDocker(){

const blob = new Blob([dockerData], {type:"text/plain"})
const url = URL.createObjectURL(blob)

const a = document.createElement("a")
a.href = url
a.download = "Dockerfile"
a.click()

}