<template>
    <div class="container-1">
    <h1>Examples</h1>
    <p class="pt">Here some interesting search queries</p>
    <div class="tab">
      <input type="radio" name="acc" id="acc1">
      <label for="acc1">
        <h2>01</h2>
        <h3>Player</h3>
      </label>
      <div class="content">
          <p>Lebron James Points</p>
          <p>Stephen Curry and Kevin Durant</p>
          <p>Damontis Sabonis Rebounds</p>
      </div>
    </div>
    <div class="tab">
      <input type="radio" name="acc" id="acc2">
      <label for="acc2">
        <h2>02</h2>
        <h3>Teams</h3>
      </label>
      <div class="content">
        <p></p>
        <p></p>
        <p></p>
      </div>
    </div>
  </div>
</template>
<script>
    export default {
        name: 'ExamplesPage'
    }
</script>
<style scoped>
  /* Examples component  */
.container-1 {
    margin: 0 40px;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    position: absolute;
    top: auto;
    left: 35%;
}

.container-1 h1 {
    background-image: linear-gradient(320deg, rgba(63,136,197,1) 39%, rgba(208,0,0,1) 56%);
    -webkit-background-clip: text;
    color: transparent;
    text-align: center;
}

.container-1 .pt {
    text-align: center;
}

.container-1 .tab {
    position: relative;
    background: #fff;
    padding: 0 20px 20px;
    box-shadow: 0 15px 25px rgba(0,0,0,0.05);
    border-radius: 5px;
    overflow: hidden;
}

.container-1 .tab input {
    appearance: none; 
}

.container-1 .tab label {
    display: flex;
    align-items: center;
    cursor: pointer;
}

.container-1 .tab label::after {
    content: '+';
    position: absolute;
    right: 0;
    font-size: 2em;
    color: rgba(0,0,0,0.1);
    transition: transform 1s;
}

.container-1 .tab:hover label::after{
    color: #333;
}

.container-1 .tab input:checked ~ label::after{
    transform: rotate(135deg);
    color: #fff;
}

.container-1 .tab label h2 {
    width: 40px;
    height: 40px;
    background: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    font-size: 1.25em;
    border-radius: 5px;
    margin-right: 10px;
}

.container-1 .tab input:checked ~ label h2 {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: rgba(255,255,255,0.2);
    font-size: 8em;
    justify-content: flex-end;
    padding: 20px;
}

.container-1 .tab:nth-child(3) label h2 {
    background: linear-gradient(135deg, #3c8ce7, #00eaff);
}

.container-1 .tab:nth-child(4) label h2 {
    background: linear-gradient(135deg, #3c8ce7, #00eaff);
}

.container-1 .tab:nth-child(5) label h2 {
    background: linear-gradient(135deg, #3c8ce7, #00eaff);
}

.container-1 .tab label h3 {
    position: relative;
    font-weight: 500;
    color: #333;
    z-index: 10;
}

.container-1 .tab .content {
    max-height: 0;
    transition: 1s;
    overflow: hidden;
}

.container-1 .tab input:checked ~ .content {
    max-height: 100vh;
}

.container-1 .tab .content p {
    position: relative;
    padding: 10px 0;
    color: #333;
    z-index: 10;
}

</style>