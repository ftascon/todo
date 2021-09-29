import axios from "axios"

const API_URL = "http://127.0.0.1:5000/tasks"

async function getAll() {
    const { data: tasks } = await axios.get(API_URL)
    return tasks
}

async function create(content) {
  const { data: data} = await axios.post(API_URL, {
    "content": content
  })
  return data.taskId
}

async function complete(id) {
  const { data: taskId } = await axios.post(`${API_URL}/complete`, {"id": id})
  return taskId
}

async function update(id, newContent) {
  const { data: newTodo } = await axios.put(`${API_URL}/${id}`, {
    content: newContent
  })
  return newTodo
}

async function remove(id) {
  await axios.delete(`${API_URL}/${id}`)
}

export default { getAll, create, completed, update, remove }