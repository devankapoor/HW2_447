import React, { useState, useEffect } from 'react'

function App()  {
  const [data, setData] = useState([{}])
  
  useEffect(() => {
    fetch("/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  },  [])

  return (
    <div>
//       <h1>Example Table</h1>
//       <table>
//         <thead>
//           <tr>
//             <th>Name</th>
//             <th>Points</th>
//             <th>Id</th>
//           </tr>
//         </thead>
//         <tbody>
//           {data.map(row => (
//             <tr key={row.id}>
//               <td>{row.name}</td>
//               <td>{row.points}</td>
//               <td>
//                 <a href={'/edit/' + row.id}>Edit</a>
//                 <a href={'/delete/' + row.id}>Delete</a>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//       <a href="/add">Add New Record</a>
    </div>
  )
}


export default App;
