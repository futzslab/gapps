<h1 align="center">GAPPS</h1>
<p align="center">
<img height="100px" src="https://www.gstatic.com/images/icons/material/system/1x/pets_black_48dp.png">
</p>

<p align="center"> Your library to help you to <br><b>Build Google Workspace add-ons in Python  🐍 !!!</b>

<p align="center">
***
</p>

[Google Workspace add-ons](https://developers.google.com/workspace/add-ons/how-tos/building-gsuite-addons) are the extensions that can be found in the side panel of most Google apps (Gmail, Google Drive, Sheets, Docs, Slides, etc), unlike the more complex [Editor add-ons](https://developers.google.com/workspace/add-ons/how-tos/building-editor-addons) that can be found in the "Add-ons" tab of Google Sheets, Docs and Slides.

| Addons             |  App Script Styple | Pythonic Style |
:-------------------------:|:-------------------------:|:-------------------------:|
![](https://developers.google.com/apps-script/add-ons/images/workspace-addons-cats.png)  |  ![]() | ![]() |

## Getting Started

<table align="center">
    <tr>
      <td align="center"><b>Deployment</b></td>
      <td align="center"><a href="https://pypi.org/project/gapps/"><img src="https://img.shields.io/pypi/v/gapps.svg?logo=python&logoColor=white" alt="pypi gapps"></a></td>
    </tr>
    <tr>
      <td align="center"><b>Build Status</b></td>
      <td align="center"><a href="https://github.com/skoudoro/gapps/actions?query=workflow%3ATest"><img src="https://github.com/skoudoro/gapps/actions/workflows/test.yml/badge.svg"></a></td>
    </tr>
    <tr>
      <td align="center"><b>Metrics</b></td>
      <td align="center">
        <a href="https://app.codacy.com/manual/skab12/gapps?utm_source=github.com&utm_medium=referral&utm_content=skoudoro/gapps&utm_campaign=Badge_Grade_Dashboard"><img src="https://api.codacy.com/project/badge/Grade/9c17e95d29cd489ba86411db969a576e" alt="codacy gapps python"></a>
<!-- <a href="https://codecov.io/gh/skoudoro/gapps"><img src="https://codecov.io/gh/skoudoro/gapps/branch/master/graph/badge.svg" alt="codecov gapps python"></a>  -->
      </td>
    </tr>
    <tr>
      <td align="center"><b>License</b></td>
      <td align="center"><a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT"></a></td>
    </tr>
    <tr>
      <td align="center"><b>Community</b></td>
      <td align="center"> <a href="https://github.com/skoudoro/gapps/blob/master/CONTRIBUTING.rst"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a> <a href="https://github.com/skoudoro/gapps/blob/master/CONTRIBUTING.rst"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a></td>
    </tr>
</table>
<!-- <a href="https://github.com/skoudoro/gapps/graphs/contributors"><img src="https://img.shields.io/github/contributors/skoudoro/gapps.svg"></a> -->



### Installation

This client is hosted at [PyPi](https://pypi.org/project/gapps/) under the name **gapps**, to install it, simply run

```terminal
pip install gapps
```

or install dev version:

```terminal
git clone https://github.com/skoudoro/gapps.git
pip install -e .
````

## Method reference

For the complete reference, visit the [official Google Workspace Add Ons API reference](https://developers.google.com/apps-script/reference/card-service).

## Notes

We still need to handle some widgets/builders but 90% of them are working correctly

we are currently updating the project to handle the new V2 released last summer 2022.

<!-- ## Features -->

## Tests

* Step 1: Install pytest

```terminal
  pip install pytest
```

* Step 2: Run the tests

```terminal
  pytest -svv gapps
```

## Contribute

We love contributions!

You've discovered a bug or something else you want to change - excellent! [Create an issue](https://github.com/skoudoro/gapps/issues)!

You've worked out a way to fix it – even better! Submit a [Pull Request](https://github.com/skoudoro/gapps/pulls)!

Start with the [contributing guide](https://github.com/skoudoro/gapps/blob/master/CONTRIBUTING.rst)!

## License

Project under MIT license, more information [here](https://github.com/skoudoro/gapps/blob/master/LICENSE)
