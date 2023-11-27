# Secret Handler for Python2

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Installing

On Debian or RedHat based systems, get the 
[latest version of the package](https://github.com/terminate-notice/secret-handler-py3/releases/latest)
and install it. 

## Using it

Run `python secret_handler.py3` with the following options:

|Short|Long|Environment|Description|
|--|--|--|--|
| `-r` | `--region` | `AWS_REGION` | The AWS region of the Secrets Manager service to call. |
| `-i` | `--id` | `SECRET_ID` | The ID (or "name") of the secret to retrieve. |
| `-k` | `--key` | `SECRET_KEY` | The secret key/value key. |

The environment variable will be overriden by the short or long arguments.

## License

This code is released under the MIT license.

## Contact

* For any issues or improvement suggestions, please 
[raise an issue](https://github.com/terminate-notice/terminate-notice/issues)!
* Want to make a change (very welcome!)? Please make pull requests!
* Found a security issue? Please
[contact me directly](mailto:jon@sprig.gs?subject=terminate-notice-security).

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://jon.sprig.gs/"><img src="https://avatars.githubusercontent.com/u/228671?v=4?s=100" width="100px;" alt="Jon "The Nice Guy" Spriggs"/><br /><sub><b>Jon "The Nice Guy" Spriggs</b></sub></a><br /><a href="https://github.com/terminate-notice/terminate-notice/commits?author=JonTheNiceGuy" title="Code">💻</a> <a href="#ideas-JonTheNiceGuy" title="Ideas, Planning, & Feedback">🤔</a> <a href="#plugin-JonTheNiceGuy" title="Plugin/utility libraries">🔌</a> <a href="#tool-JonTheNiceGuy" title="Tools">🔧</a></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td align="center" size="13px" colspan="7">
        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">
          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>
        </img>
      </td>
    </tr>
  </tfoot>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->