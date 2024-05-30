# Change Log

## [1.0.0] - 2024-05-28

### Added

- Initial release of Verbose Terminal library
- Implemented console class with logging and message styles support
- Added methods for viewing, clearing, and saving logs

## [1.0.1] - 2024-05-29

### Changed

- Renamed class `console` to `Console`.
- Created a single instance `console` of the `Console` class for global use.
- Improved `enable_logging` to include information about module, function, and line number in log messages.
- Updated the README to inform users that logging should be enabled only once, and subsequent calls will override the previous configuration.

### Fixed

- Resolved issue with simultaneous access to the log file during testing.
