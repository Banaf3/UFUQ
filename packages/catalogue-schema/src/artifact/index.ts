/** Generated catalogue artifact and provenance schemas. */

export const CATALOGUE_CANONICAL_SERIALIZATION_V1 = {
  encoding: 'UTF-8',
  byteOrderMark: false,
  unicodeNormalization: 'NFC',
  lineEnding: 'LF',
  trailingLineFeed: true,
  objectKeyOrder: 'LEXICOGRAPHIC_ASCENDING',
  recordOrder: 'HIP_ID_NUMERIC_ASCENDING',
  arrayOrder: 'SCHEMA_DEFINED',
  numberFormat: 'SHORTEST_ROUND_TRIP_JSON_NUMBER',
  negativeZero: 'NORMALIZE_TO_ZERO',
  nonFiniteNumbers: 'REJECT',
  volatileFieldsInCanonicalPayload: false,
} as const;

const sha256Pattern = '^[a-f0-9]{64}$';

export const CATALOGUE_ARTIFACT_SCHEMA_V1 = {
  $schema: 'https://json-schema.org/draft/2020-12/schema',
  $id: 'urn:ufuq:schema:artifact:catalogue:v1',
  title: 'UFUQ canonical numerical catalogue artifact',
  type: 'object',
  additionalProperties: false,
  required: ['schemaVersion', 'catalogue', 'selection', 'records'],
  properties: {
    schemaVersion: { const: 1 },
    catalogue: {
      type: 'object',
      additionalProperties: false,
      required: ['catalogueId', 'tableId', 'archiveVariant', 'referenceFrame', 'referenceEpoch'],
      properties: {
        catalogueId: { const: 'CDS_I311' },
        tableId: { const: 'hip2.dat' },
        archiveVariant: { const: 'AUTHOR_REPLACEMENT_2008-09-16' },
        referenceFrame: { const: 'ICRS' },
        referenceEpoch: {
          type: 'object',
          additionalProperties: false,
          required: ['value', 'sourceNotation', 'timeScale'],
          properties: {
            value: { const: 1991.25 },
            sourceNotation: { const: 'Ep=1991.25' },
            timeScale: { const: 'UNSPECIFIED_BY_I311_METADATA' },
          },
        },
      },
    },
    selection: {
      type: 'object',
      additionalProperties: false,
      required: ['selectionId', 'approvalStatus', 'hipIds'],
      properties: {
        selectionId: { type: 'string', minLength: 1 },
        approvalStatus: {
          enum: ['TECHNICAL_CANDIDATE_ONLY', 'DOMAIN_APPROVED'],
        },
        hipIds: {
          type: 'array',
          minItems: 1,
          uniqueItems: true,
          items: { type: 'integer', minimum: 1, maximum: 999999 },
        },
      },
    },
    records: {
      type: 'array',
      minItems: 1,
      items: { $ref: 'urn:ufuq:schema:catalogue:hipparcos-i311-main-record:v1' },
    },
  },
} as const;

export const CATALOGUE_PROVENANCE_MANIFEST_SCHEMA_V1 = {
  $schema: 'https://json-schema.org/draft/2020-12/schema',
  $id: 'urn:ufuq:schema:manifest:catalogue-provenance:v1',
  title: 'UFUQ catalogue provenance manifest',
  type: 'object',
  additionalProperties: false,
  required: [
    'schemaVersion',
    'source',
    'licence',
    'selection',
    'generator',
    'schemas',
    'canonicalSerialization',
    'artifact',
  ],
  properties: {
    schemaVersion: { const: 1 },
    source: {
      type: 'object',
      additionalProperties: false,
      required: [
        'catalogueId',
        'tableId',
        'archiveVariant',
        'sourceUrl',
        'documentationUrls',
        'acquiredAtUtc',
        'acquisitionMethod',
        'rawFiles',
        'acquisitionProvenanceStatus',
      ],
      properties: {
        catalogueId: { const: 'CDS_I311' },
        tableId: { const: 'hip2.dat' },
        archiveVariant: { const: 'AUTHOR_REPLACEMENT_2008-09-16' },
        sourceUrl: { type: 'string', minLength: 1 },
        documentationUrls: {
          type: 'array',
          minItems: 1,
          uniqueItems: true,
          items: { type: 'string', minLength: 1 },
        },
        acquiredAtUtc: {
          type: 'string',
          pattern: '^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?Z$',
        },
        acquisitionMethod: { type: 'string', minLength: 1 },
        rawFiles: {
          type: 'array',
          minItems: 1,
          items: {
            type: 'object',
            additionalProperties: false,
            required: ['relativePath', 'byteLength', 'recordCount', 'recordWidth', 'sha256'],
            properties: {
              relativePath: { type: 'string', minLength: 1 },
              byteLength: { type: 'integer', minimum: 1 },
              recordCount: { type: 'integer', minimum: 1 },
              recordWidth: { type: 'integer', minimum: 1 },
              sha256: { type: 'string', pattern: sha256Pattern },
            },
          },
        },
        acquisitionProvenanceStatus: {
          enum: ['VERIFIED', 'PARTIAL', 'UNVERIFIED'],
        },
      },
    },
    licence: {
      type: 'object',
      additionalProperties: false,
      required: ['useStatus', 'termsUrls', 'requiredAttribution', 'redistributionDecision'],
      properties: {
        useStatus: {
          enum: [
            'LOCAL_SCIENTIFIC_USE_ONLY',
            'REDISTRIBUTION_UNRESOLVED',
            'REDISTRIBUTION_APPROVED',
            'USE_NOT_PERMITTED',
          ],
        },
        termsUrls: {
          type: 'array',
          minItems: 1,
          uniqueItems: true,
          items: { type: 'string', minLength: 1 },
        },
        requiredAttribution: {
          type: 'array',
          minItems: 1,
          uniqueItems: true,
          items: { type: 'string', minLength: 1 },
        },
        redistributionDecision: {
          enum: ['BLOCK_TRACKING_AND_DEPLOYMENT', 'APPROVED'],
        },
      },
    },
    selection: {
      type: 'object',
      additionalProperties: false,
      required: ['selectionId', 'hipIds', 'approvalStatus', 'evidenceRecord'],
      properties: {
        selectionId: { type: 'string', minLength: 1 },
        hipIds: {
          type: 'array',
          minItems: 1,
          uniqueItems: true,
          items: { type: 'integer', minimum: 1, maximum: 999999 },
        },
        approvalStatus: {
          enum: ['TECHNICAL_CANDIDATE_ONLY', 'DOMAIN_APPROVED'],
        },
        evidenceRecord: { type: 'string', minLength: 1 },
      },
    },
    generator: {
      type: 'object',
      additionalProperties: false,
      required: ['name', 'version', 'gitCommit'],
      properties: {
        name: { type: 'string', minLength: 1 },
        version: { type: 'string', minLength: 1 },
        gitCommit: { type: 'string', pattern: '^[a-f0-9]{40}$' },
      },
    },
    schemas: {
      type: 'array',
      minItems: 1,
      uniqueItems: true,
      items: { type: 'string', minLength: 1 },
    },
    canonicalSerialization: {
      const: CATALOGUE_CANONICAL_SERIALIZATION_V1,
    },
    artifact: {
      type: 'object',
      additionalProperties: false,
      required: ['relativePath', 'byteLength', 'recordCount', 'sha256'],
      properties: {
        relativePath: { type: 'string', minLength: 1 },
        byteLength: { type: 'integer', minimum: 1 },
        recordCount: { type: 'integer', minimum: 1 },
        sha256: { type: 'string', pattern: sha256Pattern },
      },
    },
  },
} as const;
