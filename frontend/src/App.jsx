import React, { useState, useEffect } from "react"
import taskHttpService from "./services/taskHttpService"

import "./styles/App.css"
import "./styles/Todo-list.css"
import "./styles/Todo-create.css"
import "./styles/Checkbox.css"
import "./styles/RemoveButton.css"

function App() {
  const [tasks, setTasks] = useState([])
  const [taskContent, setTaskContent] = useState("")

  useEffect(() => {
    getAll()
  }, [])

  const getAll = async () => {
    const tasks = await taskHttpService.getAll()
    setTasks(tasks)
  }

  const handleCreate = async e  => {
    e.preventDefault()
    if(taskContent === "") {
      return false
    }
    let taskId = await taskHttpService.create(taskContent)
    let task = {
      "id": taskId,
      "content": taskContent,
      "completed": false
    }
    setTasks([...tasks, task])
    setTaskContent("")
  }

  const handleCompleted = async (e, id)  => {
    e.preventDefault()
    let taskId = await taskHttpService.completed(id)
    let taskToComplete = tasks.find(task => task.id === id)
    taskToComplete.completed = true
    setTasks( tasks.map( task => 
        (task.id === taskId ? taskToComplete : task ) 
      )
    )
  }

  const handleUpdate =  async (e, id, newContent)  => {
    e.preventDefault()
    let taskId = await taskHttpService.update(id, newContent)
    let taskToUpdate = tasks.find(task => task.id === id)
    taskToUpdate.content = newContent
    setTasks( tasks.map( task => 
        (task.id === taskId ? taskToUpdate : task ) 
      )
    )
  }

  const handleRemove = (e, id)  => {
    e.preventDefault()
    taskHttpService.remove(id)
    setTasks( tasks.filter( task => task.id !== id ) )
  }

  return (
    <div className="app">
      <div className="todo-create">
        <input 
          type="text"  
          value={taskContent}
          onChange={({ target }) => setTaskContent(target.value)}
          placeholder="Get some carrots" 
        />
        <button onClick={handleCreate}>ADD</button>
      </div>
      <div className="todo-list">
        <ul>
          {
            tasks.map((item, i) => (
              <li key={i} className={item.completed ? "completed" : ""} >
                  <p>
                    <span className="checkbox" >
                      <input type="checkbox" 
                        id={"box-" + item.id}
                        checked={item.completed ? true : false} 
                        onChange={(e) => handleCompleted(e, item.id)}
                        />
                      <label htmlFor={"box-" + item.id}></label>
                    </span>
                    {item.content}
                  </p>
                  <span className="removeButton">
                    <span 
                      className="remove"
                      onClick={(e) => handleRemove(e, item.id)}
                    ></span>
                  </span>
              </li>
            ))
          }
        </ul>
      </div>
    </div>
  );
}

export default App;
