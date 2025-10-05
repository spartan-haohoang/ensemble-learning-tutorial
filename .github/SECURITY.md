# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do not** create a public GitHub issue
2. Email the maintainers directly at [your-email@example.com]
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Response Timeline

- We will acknowledge receipt of your report within 48 hours
- We will provide a detailed response within 7 days
- We will keep you informed of our progress

## Security Best Practices

When using this project:

1. Keep your dependencies updated
2. Use the latest version of Python
3. Run security scans regularly
4. Follow the principle of least privilege
5. Use environment variables for sensitive configuration

## Security Tools

This project includes several security tools:

- **Bandit**: Static analysis for security issues
- **Safety**: Checks for known security vulnerabilities
- **Dependabot**: Automated dependency updates
- **Trivy**: Container vulnerability scanning

Run security checks with:

```bash
make security-scan
```
