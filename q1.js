// const f = (firstName, callback) => {
//   setTimeout(() => {
//     if (!firstName) return callback(new Error('firstName is required'))
//     const fullName = `${firstName} Smith`
//     return callback(fullName)
//   }, 2000)
// }

// f('Andrew', console.log)
// f(null, console.log)

const printName = (firstName) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!firstName) reject(new Error('firstName is required'))
      const fullName = `${firstName} Smith`
      resolve(fullName)
    }, 2000)
  })
}

const print = result => console.log(result)

printName('Andrew')
  .then(value => print(value))

printName(null)
  .catch(value => print(value))

