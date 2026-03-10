const users = [
    {id:1, name: 'Alice'},
    {id:2, name: 'Bob'},
    {id:3, name: 'Charlie'}
]

const newUser = users.push({id:4, name: 'David'})
console.log(users)

const filterUsers = users.find(user => user.id === 2)
console.log(filterUsers)