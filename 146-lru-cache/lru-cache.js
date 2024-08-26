class Node {
    constructor(key, value){
        this.key = key
        this.value = value
        this.left = null
        this.right = null
    }
}

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.cap = capacity
    this.cache = new Map()
    this.left = new Node(0, 0)
    this.right = new Node(0, 0)
    this.left.right = this.right
    this.right.left =this.left
};

LRUCache.prototype.remove = function(node){
    const left = node.left, right = node.right

    left.right = right
    right.left = left
}

LRUCache.prototype.add = function(node){
    const left = this.right.left, right = this.right

    left.right = node
    right.left = node
    node.left = left
    node.right = right
}

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if(this.cache.has(key)){
        const node = this.cache.get(key)
        this.remove(node)
        this.add(node)
        return node.value
    }
    return -1
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if(this.cache.has(key)){
        this.remove(this.cache.get(key))
    }
    const newNode = new Node(key, value)
    this.cache.set(key, newNode)
    this.add(newNode)
    if(this.cache.size > this.cap){
        const lru = this.left.right
        this.remove(lru)
        this.cache.delete(lru.key)
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */