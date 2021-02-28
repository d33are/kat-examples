[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <pre align="center"> 
    @@@  @@@  @@@@@@  @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@  @@@ @@@  @@@ @@@@@@@@ 
    @@!  !@@ @@!  @@@   @!!   @@!  @@@ @@!      @@!  @@@ @@! @@!@!@@@ @@!      
    @!@@!@!  @!@!@!@!   @!!   @!@!@!@! @!!!:!   @!@!!@!  !!@ @!@@!!@! @!!!:!   
    !!: :!!  !!:  !!!   !!:   !!:  !!! !!:      !!: :!!  !!: !!:  !!! !!:      
     :   :::  :   : :    :     :   : : : :: ::   :   : : :   ::    :  : :: ::  
  </pre>

  <h3 align="center">kat-examples</h3>

  <p align="center">
    Katherine framework example scenarios
    <br />
    <a href="https://github.com/d33are/kat-examples"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/d33are/kat-examples">View Demo</a>
    ·
    <a href="https://github.com/d33are/kat-examples/issues">Report Bug</a>
    ·
    <a href="https://github.com/d33are/kat-examples/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#optional-dependencies">Optional dependencies</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
        <ul>
          <li><a href="#example-configurations">Example configurations</a></li>
          <li><a href="#scenario-execution">Scenario execution</a></li>
        </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Katherine is a general framework for playing video games with deep learning agents. This is a "home project" like framework, so it is currently under development, and it might have some bugs ( ¯\\\_(ツ)_/¯ ). It was not aimed for professional use, I'm just making this framework for educational purposes.

The main goal of the framework is to be simple as possible, and able to use it without any, or with very basic coding skills. The hole framework can be configured by `yaml` files, so for creating a new game scenario, you only need to create a configuration file and run it.

This repository is contains a few example scenarios, and an example entry point.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of "how to check your python version."
  ```sh
  python --version
  ```
3.8 >= `python version` >= 3.7 will be fine.

Check kat-framework installation:
```sh
pip show kat-framework
Name: kat-framework
Version: 1.0.0
Summary: Katherine A.I. framework
```
_For more detailed information about kat-framework installation, please refer to the [Documentation][kat-framewrok-url]._

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/d33are/kat-examples.git
   ```

### Optional dependencies

* For tensorflow backend, please install tensorflow: [Installing Tensorflow][install-tensorflow]
* For playing with zDoom, please install VizDoom: [Installing zDoom][install-vizdoom]
* For playing with OpenAI gym games, please install gym: [Installing gym][install-gym]

_Implementations are included in the framework, just installations are needed._

<!-- USAGE EXAMPLES -->
## Usage

### Example configurations

This repo is containing the following config structure:
```sh
kat-examples
|  |- scenarios
|  |  |- openai
|  |  |  |- img
|  |  |  |  |- atari_breakout
|  |  |  |  |  |- atari_breakout.yaml
|  |  |  |  |- atari_pong
|  |  |  |  |  |- atari_pong.yaml
|  |  |  |  |- atari_space_invaders
|  |  |  |  |  |- atari_space_invaders.yaml
|  |  |  |  |- img.yaml
|  |  |  |- ram
|  |  |  |  |- atari_breakout
|  |  |  |  |  |- atari_breakout.yaml
|  |  |  |  |- atari_pong
|  |  |  |  |  |- atari_pong.yaml
|  |  |  |  |- atari_space_invaders
|  |  |  |  |  |- atari_space_invaders.yaml
|  |  |  |  |- lunar_lander
|  |  |  |  |  |- lunar_lander.yaml
|  |  |  |  |- ram.yaml
|  |  |- zdoom
|  |  |  |- defend_the_line
|  |  |  |  |- defend_the_line.yaml
|  |  |  |- simpler_basic
|  |  |  |  |- simpler_basic.yaml
|  |  |  |- zdoom.yaml
|  |  |- default.yaml
```
_For more information about the hierarchical config, please refer to the [Documentation][himl-documentation]._

### Scenario execution

For executing a scenario, you only need to specify the configuration with the `--config_uri` cli-option:
```sh
cd kat-examples
```
```sh
python main.py --config_uri="file://localhost/scenarios/openai/ram/lunar_lander"
```

This will runs the lunar lander scenario with the specified configuration.

<!-- ROADMAP -->
## Roadmap

See the [open issues][issues-url] for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

d33are - `d33are[at]gmail[dot]com`

Project Link: [https://github.com/d33are/kat-examples][project-link]


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/d33are/kat-examples.svg?style=for-the-badge
[license-url]: https://github.com/d33are/kat-examples/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dkaszas
[issues-url]: https://github.com/d33are/kat-examples/issues
[project-link]: https://github.com/d33are/kat-examples
[himl-documentation]: https://github.com/adobe/himl
[install-tensorflow]: https://www.tensorflow.org/install/
[install-vizdoom]: https://github.com/mwydmuch/ViZDoom
[install-gym]: https://gym.openai.com/docs/
[kat-framewrok-url]: https://github.com/d33are/kat-framework