const myKey = 'key';

const website = {
    name: 'Alabala',
    rating: 5,
    founders: ['Ivan', 'Maria'],
    isAlabala: true,
    // [myKey]: 1234,
};

console.log(website.name);

// website.name = 'Edited';
// console.log(website.name);
// website.foo = 'bar';
// console.log(website);
// delete website.foo;
// console.log(website);

// const obj = {}
// console.log(obj === obj});

// const name = 'Ivan';
// const obj = {
//     name, 
// }

// console.log(obj);

// const obj = new Object();
// obj.name = 'Ivan';
// console.log(obj.name);

// function Website(name, rating, founders) {
//     this.name = name;
//     this.rating = rating;
//     this.founders = founders;
// }

// const artwoodique = new Website('Artwoodique', 5, ['ivan', 'mariqn']);
// console.log(artwoodique);


// const id = Symbol('id');
// const id2 = Symbol('id2');
// const id3 = Symbol.for('id3');
// const id4 = Symbol.for('id3');

// // console.log(id3 == id4)

// // const obj = {
// //     [id]: 1234,
// // }

// // console.log(obj);

// console.log('name' in website);
// console.log(website.hasOwnProperty('name'));
// console.log(website.name !== undefined);

const website1 = {
    name: 'ivan',
    rating: 5,
    founders: ['ivan', 'mariqn'],
    sayhello() {
        console.log('hello');
    },

    get getRating() {
        return this.rating;
    },
    set setRating(value) {
        this.rating = value;
    }
};
website1.sayhello();

const objWebsite = {
    __proto__: website,
    [Symbol['id']]: 0,
    foo: 'bar',
}

// console.log(objWebsite);
// console.log(objWebsite);
console.log(Object.keys(objWebsite));